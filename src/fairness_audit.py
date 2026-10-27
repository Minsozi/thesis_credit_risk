"""
Stage 12 — Fairness & Responsible AI Audit
==========================================
Candidate : Percyviarance Minsozi Simasiku (201061589)
Supervisor : Mrs. Johanna Nelulu, Dept Computer Science, UNAM
Date       : 2026-09-20

Audits XGBoost (primary) and Random Forest (secondary) against three protected
attributes:
  - gender             (Female vs Male)
  - urban_rural        (Rural vs Urban)
  - business_registration_status (Informal vs Formal)

Metrics computed:
  - Demographic Parity Difference (DPD)
  - Disparate Impact Ratio (DIR)  — four-fifths rule flag if DIR < 0.80
  - Equal Opportunity Difference  (EOD) — TPR gap
  - False Negative Rate (FNR) by group — credit-inclusion fairness lens
  - Accuracy by group

Threshold mitigation:
  - If DIR < 0.80 for any group, per-group threshold is tuned to equalise
    approval rates and the fairness-accuracy Pareto frontier is reported.

Outputs (all to results/ and figures/):
  results/fairness_audit_report.json
  figures/fairness_approval_rates.png
  figures/fairness_dir_comparison.png
  figures/fairness_fnr_by_group.png
  figures/fairness_pareto_frontier.png   (generated only if mitigation triggered)
"""

import json, warnings
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import joblib

warnings.filterwarnings("ignore")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE   = Path(r"C:\Users\201061589\Documents\thesis_credit_risk")
DATA   = BASE / "data" / "processed"
MODELS = BASE / "models"
FIGS   = BASE / "figures"
RES    = BASE / "results"
FIGS.mkdir(exist_ok=True)
RES.mkdir(exist_ok=True)

SEED = 42
THRESHOLD_DEFAULT = 0.5

# ── Load artefacts ─────────────────────────────────────────────────────────────
print("Loading data …")
X_test   = pd.read_csv(DATA / "test_features.csv")
y_test   = pd.read_csv(DATA / "test_target.csv").squeeze()
prot     = pd.read_csv(DATA / "protected_attributes_test.csv")

# Align index
X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)
prot   = prot.reset_index(drop=True)

print(f"Test set : {X_test.shape[0]} rows, {X_test.shape[1]} features")
print(f"Defaults : {y_test.sum()} ({y_test.mean()*100:.2f}%)")
print("Protected attributes:\n", prot.head(3))

print("\nLoading models …")
xgb = joblib.load(MODELS / "advanced_xgboost.joblib")
rf  = joblib.load(MODELS / "advanced_random_forest.joblib")

# ── Probability predictions ────────────────────────────────────────────────────
prob_xgb = xgb.predict_proba(X_test)[:, 1]
prob_rf  = rf.predict_proba(X_test)[:, 1]

# ── Helper functions ───────────────────────────────────────────────────────────

def group_metrics(y_true, y_prob, group_series, threshold=0.5):
    """
    Returns a DataFrame: one row per group value with columns:
    n, n_pos, approval_rate, tpr, fnr, fpr, accuracy, dpd, dir_, eod
    """
    y_pred = (y_prob >= threshold).astype(int)
    rows = []
    groups = sorted(group_series.unique())
    for g in groups:
        mask = group_series == g
        yt = y_true[mask].values
        yp = y_pred[mask]
        pp = y_prob[mask]
        n = mask.sum()
        pos = yt.sum()
        tp = ((yp == 1) & (yt == 1)).sum()
        fp = ((yp == 1) & (yt == 0)).sum()
        fn = ((yp == 0) & (yt == 1)).sum()
        tn = ((yp == 0) & (yt == 0)).sum()
        approval = yp.mean()
        tpr = tp / pos if pos > 0 else np.nan
        fnr = fn / pos if pos > 0 else np.nan
        fpr = fp / (fp + tn) if (fp + tn) > 0 else np.nan
        acc = (tp + tn) / n
        rows.append(dict(group=g, n=int(n), n_defaults=int(pos),
                         approval_rate=round(approval, 4),
                         tpr=round(tpr, 4) if not np.isnan(tpr) else None,
                         fnr=round(fnr, 4) if not np.isnan(fnr) else None,
                         fpr=round(fpr, 4) if not np.isnan(fpr) else None,
                         accuracy=round(acc, 4)))
    df = pd.DataFrame(rows).set_index("group")
    return df


def fairness_summary(df, privileged, unprivileged, attribute):
    """Given group_metrics df, compute pairwise DPD, DIR, EOD."""
    if privileged not in df.index or unprivileged not in df.index:
        return {}
    ar_priv   = df.loc[privileged,   "approval_rate"]
    ar_unpriv = df.loc[unprivileged, "approval_rate"]
    tpr_priv   = df.loc[privileged,   "tpr"]
    tpr_unpriv = df.loc[unprivileged, "tpr"]
    fnr_priv   = df.loc[privileged,   "fnr"]
    fnr_unpriv = df.loc[unprivileged, "fnr"]
    dpd = round(float(ar_unpriv - ar_priv), 4)
    dir_ = round(float(ar_unpriv / ar_priv), 4) if ar_priv > 0 else None
    eod = round(float((tpr_unpriv or 0) - (tpr_priv or 0)), 4)
    fnr_gap = round(float((fnr_unpriv or 0) - (fnr_priv or 0)), 4)
    flag_dir = dir_ is not None and dir_ < 0.80
    flag_eod = abs(eod) > 0.10
    return dict(attribute=attribute, privileged=privileged,
                unprivileged=unprivileged,
                approval_rate_privileged=float(ar_priv),
                approval_rate_unprivileged=float(ar_unpriv),
                dpd=dpd, dir=dir_,
                eod=eod, fnr_gap=fnr_gap,
                four_fifths_violated=flag_dir,
                eod_flag=flag_eod)


# ── Audit configuration ────────────────────────────────────────────────────────
AUDIT_PAIRS = [
    ("gender",                     "Male",   "Female"),
    ("urban_rural",                "Urban",  "Rural"),
    ("business_registration_status", "Formal", "Informal"),
]

# Decode business_registration_status: 1 → Formal, 0 → Informal
if "business_registration_status" in prot.columns:
    prot["business_registration_status"] = (
        prot["business_registration_status"]
        .map({1: "Formal", 0: "Informal"})
        .fillna(prot["business_registration_status"].astype(str))
    )

MODELS_TO_AUDIT = {
    "XGBoost": prob_xgb,
    "Random Forest": prob_rf,
}

# ── Run audit ──────────────────────────────────────────────────────────────────
report = {
    "candidate": "Percyviarance Minsozi Simasiku",
    "student_id": "201061589",
    "threshold_used": THRESHOLD_DEFAULT,
    "models": {}
}

all_group_dfs = {}   # keyed by (model_name, attribute)

for model_name, probs in MODELS_TO_AUDIT.items():
    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    model_report = {"fairness_pairs": [], "group_metrics": {}}

    for attr, privileged, unprivileged in AUDIT_PAIRS:
        if attr not in prot.columns:
            print(f"  [WARN] {attr} not in protected attributes file — skipping")
            continue
        gdf = group_metrics(y_test, probs, prot[attr], threshold=THRESHOLD_DEFAULT)
        all_group_dfs[(model_name, attr)] = gdf
        fs  = fairness_summary(gdf, privileged, unprivileged, attr)
        model_report["fairness_pairs"].append(fs)
        model_report["group_metrics"][attr] = gdf.reset_index().to_dict(orient="records")

        print(f"\n  Attribute: {attr}")
        print(gdf[["n","n_defaults","approval_rate","tpr","fnr","accuracy"]].to_string())
        if fs and "dpd" in fs:
            dir_v = fs['dir']
            dir_s = f"{dir_v:.4f}" if dir_v is not None else "N/A"
            print(f"  DPD={fs['dpd']:.4f}  DIR={dir_s}  EOD={fs['eod']:.4f}  "
                  f"FNR-gap={fs['fnr_gap']:.4f}  4/5-violated={fs['four_fifths_violated']}")
        else:
            print("  [WARN] Fairness summary could not be computed for this attribute.")


    report["models"][model_name] = model_report

# ── Threshold Mitigation ───────────────────────────────────────────────────────
print("\n\nThreshold Mitigation Analysis (XGBoost, four-fifths rule)…")

mitigation_results = []
NEEDS_MITIGATION = False

for fs in report["models"]["XGBoost"]["fairness_pairs"]:
    if fs.get("four_fifths_violated"):
        NEEDS_MITIGATION = True
        attr       = fs["attribute"]
        unpriv     = fs["unprivileged"]
        privileged = fs["privileged"]
        print(f"  ► Mitigation triggered for {attr}: {unpriv} DIR={fs['dir']:.4f}")

        thresholds = np.arange(0.05, 0.95, 0.01)
        rows = []
        for t in thresholds:
            gdf_t = group_metrics(y_test, prob_xgb, prot[attr], threshold=t)
            if unpriv in gdf_t.index and privileged in gdf_t.index:
                ar_u = gdf_t.loc[unpriv, "approval_rate"]
                ar_p = gdf_t.loc[privileged, "approval_rate"]
                dir_t = ar_u / ar_p if ar_p > 0 else 0
                acc_u = gdf_t.loc[unpriv, "accuracy"]
                rows.append(dict(threshold=round(float(t),2),
                                 dir=round(float(dir_t),4),
                                 approval_rate_unprivileged=round(float(ar_u),4),
                                 approval_rate_privileged=round(float(ar_p),4),
                                 accuracy_unprivileged=round(float(acc_u),4)))
        pareto_df = pd.DataFrame(rows)
        # find thresholds achieving DIR >= 0.80
        fair_df = pareto_df[pareto_df["dir"] >= 0.80]
        best_row = None
        if len(fair_df) > 0:
            best_row = fair_df.loc[fair_df["accuracy_unprivileged"].idxmax()]
            print(f"    Best fair threshold for {unpriv}: t={best_row['threshold']:.2f}, "
                  f"DIR={best_row['dir']:.4f}, AccUnpriv={best_row['accuracy_unprivileged']:.4f}")
        else:
            print(f"    [WARN] No threshold achieves DIR ≥ 0.80 for {attr}")

        mitigation_results.append(dict(
            attribute=attr, unprivileged=unpriv,
            pareto_frontier=pareto_df.to_dict(orient="records"),
            recommended_threshold=float(best_row["threshold"]) if best_row is not None else None,
            recommended_dir=float(best_row["dir"]) if best_row is not None else None,
        ))

        # Pareto frontier figure
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(pareto_df["threshold"], pareto_df["dir"], color="#2563EB", linewidth=2,
                label="DIR vs Threshold")
        ax.axhline(0.80, color="#DC2626", linestyle="--", linewidth=1.5,
                   label="Four-Fifths Threshold (0.80)")
        ax.axvline(0.5, color="#6B7280", linestyle=":", linewidth=1.2,
                   label="Standard Threshold (0.50)")
        if best_row is not None:
            ax.axvline(best_row["threshold"], color="#16A34A", linestyle="-.",
                       linewidth=1.5, label=f"Recommended t={best_row['threshold']:.2f}")
        ax.set_xlabel("Decision Threshold", fontsize=12)
        ax.set_ylabel("Disparate Impact Ratio (DIR)", fontsize=12)
        ax.set_title(f"Fairness-Accuracy Pareto Frontier\n"
                     f"{attr}: {unpriv} vs {privileged} (XGBoost)", fontsize=13)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(FIGS / f"fairness_pareto_{attr}.png", dpi=300)
        plt.close(fig)
        print(f"    Saved: figures/fairness_pareto_{attr}.png")

report["threshold_mitigation"] = mitigation_results

# ── Figure 1: Approval Rates by Group ─────────────────────────────────────────
print("\nGenerating fairness figures …")

COLORS = {"XGBoost": "#2563EB", "Random Forest": "#16A34A"}
attributes_ordered = [a for a, _, _ in AUDIT_PAIRS
                      if a in prot.columns]

fig, axes = plt.subplots(1, len(attributes_ordered), figsize=(5*len(attributes_ordered), 6))
if len(attributes_ordered) == 1:
    axes = [axes]

for ax, (attr, priv, unpriv) in zip(axes, AUDIT_PAIRS):
    x_labels = []
    xgb_vals = []
    rf_vals  = []
    gdf_x = all_group_dfs.get(("XGBoost", attr))
    gdf_r = all_group_dfs.get(("Random Forest", attr))
    if gdf_x is None:
        continue
    groups = sorted(gdf_x.index.tolist())
    x = np.arange(len(groups))
    w = 0.35
    xgb_ar = [gdf_x.loc[g, "approval_rate"] if g in gdf_x.index else 0 for g in groups]
    rf_ar  = [gdf_r.loc[g, "approval_rate"] if gdf_r is not None and g in gdf_r.index else 0 for g in groups]

    bars1 = ax.bar(x - w/2, xgb_ar, w, color=COLORS["XGBoost"], label="XGBoost", alpha=0.85)
    bars2 = ax.bar(x + w/2, rf_ar,  w, color=COLORS["Random Forest"], label="Random Forest", alpha=0.85)

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.003,
                f"{bar.get_height():.2%}", ha="center", va="bottom", fontsize=9)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.003,
                f"{bar.get_height():.2%}", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=10)
    ax.set_ylabel("Approval Rate (P(Ŷ=1))", fontsize=11)
    ax.set_title(f"{attr.replace('_', ' ').title()}", fontsize=12, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(0, max(max(xgb_ar), max(rf_ar)) * 1.2 + 0.05)

fig.suptitle("Credit Approval Rates by Protected Group\n"
             "Boa N Credit Risk Model — Namibia Fintech Sandbox",
             fontsize=14, fontweight="bold")
fig.tight_layout()
fig.savefig(FIGS / "fairness_approval_rates.png", dpi=300)
plt.close(fig)
print("Saved: figures/fairness_approval_rates.png")

# ── Figure 2: DIR Comparison ───────────────────────────────────────────────────
attr_labels = [a.replace("_", "\n").title() for a, _, _ in AUDIT_PAIRS if a in prot.columns]
dir_xgb = []
dir_rf  = []
for attr, priv, unpriv in AUDIT_PAIRS:
    if attr not in prot.columns:
        continue
    for fs in report["models"]["XGBoost"]["fairness_pairs"]:
        if fs.get("attribute") == attr:
            dir_xgb.append(fs.get("dir", 0) or 0)
    for fs in report["models"]["Random Forest"]["fairness_pairs"]:
        if fs.get("attribute") == attr:
            dir_rf.append(fs.get("dir", 0) or 0)

x = np.arange(len(attr_labels))
w = 0.35
fig, ax = plt.subplots(figsize=(9, 5))
bars1 = ax.bar(x - w/2, dir_xgb, w, color=COLORS["XGBoost"], label="XGBoost", alpha=0.85)
bars2 = ax.bar(x + w/2, dir_rf,  w, color=COLORS["Random Forest"], label="Random Forest", alpha=0.85)
ax.axhline(0.80, color="#DC2626", linestyle="--", linewidth=2, label="Four-Fifths Rule (0.80)")
ax.axhline(1.00, color="#374151", linestyle=":",  linewidth=1.2, label="Perfect Parity (1.00)")

for bar in bars1 + bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
            f"{bar.get_height():.3f}", ha="center", va="bottom", fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(attr_labels, fontsize=10)
ax.set_ylabel("Disparate Impact Ratio (DIR)", fontsize=11)
ax.set_title("Disparate Impact Ratio by Protected Attribute and Model\n"
             "(Unprivileged / Privileged Approval Rate)", fontsize=13)
ax.legend(fontsize=10)
ax.grid(axis="y", alpha=0.3)
ax.set_ylim(0, max(max(dir_xgb), max(dir_rf)) * 1.25 + 0.15)
fig.tight_layout()
fig.savefig(FIGS / "fairness_dir_comparison.png", dpi=300)
plt.close(fig)
print("Saved: figures/fairness_dir_comparison.png")

# ── Figure 3: FNR by Protected Group ──────────────────────────────────────────
fig, axes = plt.subplots(1, len(attributes_ordered), figsize=(5*len(attributes_ordered), 6))
if len(attributes_ordered) == 1:
    axes = [axes]

for ax, (attr, priv, unpriv) in zip(axes, AUDIT_PAIRS):
    gdf_x = all_group_dfs.get(("XGBoost", attr))
    gdf_r = all_group_dfs.get(("Random Forest", attr))
    if gdf_x is None:
        continue
    groups = sorted(gdf_x.index.tolist())
    x = np.arange(len(groups))
    w = 0.35
    xgb_fnr = [float(gdf_x.loc[g, "fnr"]) if g in gdf_x.index and gdf_x.loc[g, "fnr"] is not None else 0 for g in groups]
    rf_fnr  = [float(gdf_r.loc[g, "fnr"]) if gdf_r is not None and g in gdf_r.index and gdf_r.loc[g, "fnr"] is not None else 0 for g in groups]

    bars1 = ax.bar(x - w/2, xgb_fnr, w, color=COLORS["XGBoost"], label="XGBoost", alpha=0.85)
    bars2 = ax.bar(x + w/2, rf_fnr,  w, color=COLORS["Random Forest"], label="Random Forest", alpha=0.85)

    for bar in bars1 + bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f"{bar.get_height():.2%}", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=10)
    ax.set_ylabel("False Negative Rate (FNR)", fontsize=11)
    ax.set_title(f"{attr.replace('_', ' ').title()}", fontsize=12, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)

fig.suptitle("False Negative Rate by Protected Group\n"
             "(Higher FNR = creditworthy applicants incorrectly denied — inclusion harm)",
             fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(FIGS / "fairness_fnr_by_group.png", dpi=300)
plt.close(fig)
print("Saved: figures/fairness_fnr_by_group.png")

# ── Export JSON report ─────────────────────────────────────────────────────────
report_path = RES / "fairness_audit_report.json"
with open(report_path, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(f"\nSaved: results/fairness_audit_report.json")

# ── Console summary ────────────────────────────────────────────────────────────
print("\n" + "="*65)
print("FAIRNESS AUDIT SUMMARY — XGBoost @ threshold=0.50")
print("="*65)
for fs in report["models"]["XGBoost"]["fairness_pairs"]:
    if not fs or "dpd" not in fs:
        print("\n  [SKIPPED — insufficient group data]")
        continue
    attr  = fs["attribute"]
    priv  = fs["privileged"]
    unpriv = fs["unprivileged"]
    print(f"\n  {attr.upper()}  ({unpriv} vs {priv})")
    print(f"    Approval Rate: {priv}={fs['approval_rate_privileged']:.2%}  "
          f"{unpriv}={fs['approval_rate_unprivileged']:.2%}")
    dir_val = fs['dir']
    dir_str = f"{dir_val:.4f}" if dir_val is not None else "N/A"
    print(f"    DPD  = {fs['dpd']:+.4f}   DIR = {dir_str}   "
          f"{'[!] FOUR-FIFTHS VIOLATED' if fs['four_fifths_violated'] else '[OK]'}")
    print(f"    EOD  = {fs['eod']:+.4f}   FNR-gap = {fs['fnr_gap']:+.4f}   "
          f"{'[!] EOD FLAG' if fs['eod_flag'] else '[OK]'}")
print("\n" + "="*65)
print("Stage 12 complete.")

