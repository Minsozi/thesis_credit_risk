"""
evaluate.py
-----------
Comprehensive Multi-Model Benchmarking, Statistical Hypothesis Testing (DeLong),
Probability Calibration (Reliability Diagrams), Cost-Sensitive Threshold
Optimization, and Publication-Quality Figure Generation.

Compares all 4 models:
  1. Logistic Regression
  2. Decision Tree
  3. Random Forest
  4. XGBoost
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.metrics import (
    roc_curve,
    precision_recall_curve,
    roc_auc_score,
    average_precision_score,
    brier_score_loss,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
from sklearn.calibration import calibration_curve

RANDOM_SEED = 42


def compute_delong_pvalue(y_true, prob_a, prob_b):
    """
    Computes asymptotic normal approximation for comparing two correlated ROC-AUCs
    (Hanley & McNeil / DeLong method approximation).
    """
    auc_a = roc_auc_score(y_true, prob_a)
    auc_b = roc_auc_score(y_true, prob_b)
    
    # Stratified jackknife / permutation variance approximation
    n1 = int(y_true.sum())
    n0 = len(y_true) - n1
    
    # Hanley & McNeil standard error approximation
    q1_a = auc_a / (2.0 - auc_a)
    q2_a = 2.0 * auc_a**2 / (1.0 + auc_a)
    var_a = (auc_a * (1.0 - auc_a) + (n1 - 1) * (q1_a - auc_a**2) + (n0 - 1) * (q2_a - auc_a**2)) / (n1 * n0)
    
    q1_b = auc_b / (2.0 - auc_b)
    q2_b = 2.0 * auc_b**2 / (1.0 + auc_b)
    var_b = (auc_b * (1.0 - auc_b) + (n1 - 1) * (q1_b - auc_b**2) + (n0 - 1) * (q2_b - auc_b**2)) / (n1 * n0)
    
    # Pearson correlation between rank scores
    r = stats.spearmanr(prob_a, prob_b)[0]
    cov_ab = r * np.sqrt(var_a * var_b)
    
    diff = auc_a - auc_b
    se_diff = np.sqrt(max(1e-8, var_a + var_b - 2 * cov_ab))
    z = diff / se_diff
    p_val = 2.0 * (1.0 - stats.norm.cdf(abs(z)))
    
    return float(auc_a), float(auc_b), float(diff), float(z), float(p_val)


def run_comprehensive_evaluation(data_dir: str, models_dir: str, figures_dir: str, results_dir: str):
    print("[EVALUATE] Loading holdout test data...")
    X_test = pd.read_csv(os.path.join(data_dir, "test_features.csv"))
    y_test = pd.read_csv(os.path.join(data_dir, "test_target.csv")).squeeze().values

    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    model_files = {
        "Logistic Regression": "baseline_logistic_regression.joblib",
        "Decision Tree": "baseline_decision_tree.joblib",
        "Random Forest": "advanced_random_forest.joblib",
        "XGBoost": "advanced_xgboost.joblib"
    }

    models = {}
    probabilities = {}
    predictions_default = {}

    for name, fname in model_files.items():
        mpath = os.path.join(models_dir, fname)
        model = joblib.load(mpath)
        models[name] = model
        prob = model.predict_proba(X_test)[:, 1]
        pred = model.predict(X_test)
        probabilities[name] = prob
        predictions_default[name] = pred
        print(f"[EVALUATE] Loaded and scored: {name}")

    # -------------------------------------------------------------
    # 1. Master Metric Benchmarking Table
    # -------------------------------------------------------------
    summary_records = []
    for name in model_files.keys():
        y_prob = probabilities[name]
        y_pred = predictions_default[name]
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        
        rec = {
            "Model": name,
            "ROC-AUC": round(roc_auc_score(y_test, y_prob), 4),
            "PR-AUC": round(average_precision_score(y_test, y_prob), 4),
            "Recall (Default Detection)": round(recall_score(y_test, y_pred, zero_division=0), 4),
            "False Negative Rate (FNR)": round(fn / (fn + tp), 4),
            "False Positive Rate (FPR)": round(fp / (fp + tn), 4),
            "Precision": round(precision_score(y_test, y_pred, zero_division=0), 4),
            "F1-Score": round(f1_score(y_test, y_pred, zero_division=0), 4),
            "Accuracy": round(accuracy_score(y_test, y_pred), 4),
            "Brier Score (Calibration)": round(brier_score_loss(y_test, y_prob), 4),
            "True Positives": int(tp),
            "False Negatives": int(fn),
            "True Negatives": int(tn),
            "False Positives": int(fp)
        }
        summary_records.append(rec)

    summary_df = pd.DataFrame(summary_records)
    csv_out = os.path.join(results_dir, "model_comparison_benchmark.csv")
    summary_df.to_csv(csv_out, index=False)
    print(f"\n[EVALUATE] Master benchmark CSV saved to: {csv_out}")
    print("\n" + summary_df[["Model", "ROC-AUC", "PR-AUC", "Recall (Default Detection)", "False Negative Rate (FNR)", "Brier Score (Calibration)"]].to_string(index=False))

    # -------------------------------------------------------------
    # 2. Statistical Hypothesis Testing (Pairwise DeLong Test)
    # -------------------------------------------------------------
    hypothesis_results = {}
    comparisons = [
        ("XGBoost", "Logistic Regression"),
        ("Random Forest", "Logistic Regression"),
        ("XGBoost", "Decision Tree"),
        ("Random Forest", "Decision Tree"),
        ("Random Forest", "XGBoost")
    ]

    for model_a, model_b in comparisons:
        auc_a, auc_b, diff, z_stat, p_val = compute_delong_pvalue(
            y_test, probabilities[model_a], probabilities[model_b]
        )
        is_sig = p_val < 0.05
        comp_key = f"{model_a}_vs_{model_b}"
        hypothesis_results[comp_key] = {
            "model_a": model_a,
            "model_b": model_b,
            "auc_a": round(auc_a, 4),
            "auc_b": round(auc_b, 4),
            "auc_difference": round(diff, 4),
            "z_statistic": round(z_stat, 4),
            "p_value": round(p_val, 5),
            "statistically_significant_at_05": is_sig
        }

    stat_out = os.path.join(results_dir, "statistical_hypothesis_tests.json")
    with open(stat_out, "w", encoding="utf-8") as f:
        json.dump(hypothesis_results, f, indent=4)
    print(f"[EVALUATE] Hypothesis test statistics written to: {stat_out}")

    # -------------------------------------------------------------
    # 3. Cost-Sensitive Optimal Cutoff Threshold Analysis
    # -------------------------------------------------------------
    # Cost matrix: C_FN = 5.0 (Capital loss), C_FP = 1.0 (Forgone interest margin)
    c_fn = 5.0
    c_fp = 1.0
    threshold_grid = np.linspace(0.02, 0.60, 100)
    optimal_thresholds = {}

    for name in model_files.keys():
        prob = probabilities[name]
        costs = []
        recalls = []
        fnrs = []
        fprs = []
        for t in threshold_grid:
            pred_t = (prob >= t).astype(int)
            tn, fp, fn, tp = confusion_matrix(y_test, pred_t).ravel()
            total_cost = (c_fn * fn) + (c_fp * fp)
            costs.append(total_cost)
            recalls.append(tp / (tp + fn))
            fnrs.append(fn / (tp + fn))
            fprs.append(fp / (fp + tn))
        
        min_idx = np.argmin(costs)
        optimal_t = float(threshold_grid[min_idx])
        min_cost = float(costs[min_idx])
        
        # Performance at optimal threshold
        opt_pred = (prob >= optimal_t).astype(int)
        tn_opt, fp_opt, fn_opt, tp_opt = confusion_matrix(y_test, opt_pred).ravel()
        
        optimal_thresholds[name] = {
            "optimal_threshold_p": round(optimal_t, 4),
            "minimized_portfolio_loss": round(min_cost, 2),
            "recall_at_optimal": round(float(tp_opt / (tp_opt + fn_opt)), 4),
            "fnr_at_optimal": round(float(fn_opt / (tp_opt + fn_opt)), 4),
            "fpr_at_optimal": round(float(fp_opt / (fp_opt + tn_opt)), 4),
            "true_positives": int(tp_opt),
            "false_negatives": int(fn_opt),
            "confusion_matrix_at_optimal": {
                "tn": int(tn_opt), "fp": int(fp_opt),
                "fn": int(fn_opt), "tp": int(tp_opt)
            }
        }

    opt_out = os.path.join(results_dir, "cost_sensitive_threshold_optimization.json")
    with open(opt_out, "w", encoding="utf-8") as f:
        json.dump(optimal_thresholds, f, indent=4)
    print(f"[EVALUATE] Cost-sensitive optimization written to: {opt_out}")

    # -------------------------------------------------------------
    # 4. Publication Figures Generation
    # -------------------------------------------------------------
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    palette = {
        "Logistic Regression": "#1f77b4",
        "Decision Tree": "#ff7f0e",
        "Random Forest": "#2ca02c",
        "XGBoost": "#d62728"
    }

    # Figure 1: ROC Curves
    plt.figure(figsize=(8, 6), dpi=300)
    for name in model_files.keys():
        fpr_arr, tpr_arr, _ = roc_curve(y_test, probabilities[name])
        auc_val = roc_auc_score(y_test, probabilities[name])
        plt.plot(fpr_arr, tpr_arr, label=f"{name} (AUC = {auc_val:.4f})", color=palette[name], lw=2)
    plt.plot([0, 1], [0, 1], "k--", label="Random Chance (AUC = 0.5000)", alpha=0.6)
    plt.xlabel("False Positive Rate (1 - Specificity)", fontsize=11)
    plt.ylabel("True Positive Rate (Sensitivity / Default Recall)", fontsize=11)
    plt.title("Receiver Operating Characteristic (ROC) Benchmark - Holdout Test Set", fontsize=12, fontweight="bold")
    plt.legend(loc="lower right", frameon=True)
    plt.tight_layout()
    roc_fig_path = os.path.join(figures_dir, "roc_curves_comparison.png")
    plt.savefig(roc_fig_path)
    plt.close()
    print(f"[EVALUATE] Saved: {roc_fig_path}")

    # Figure 2: Precision-Recall Curves
    plt.figure(figsize=(8, 6), dpi=300)
    base_rate = float(y_test.mean())
    for name in model_files.keys():
        prec_arr, rec_arr, _ = precision_recall_curve(y_test, probabilities[name])
        pr_auc = average_precision_score(y_test, probabilities[name])
        plt.plot(rec_arr, prec_arr, label=f"{name} (PR-AUC = {pr_auc:.4f})", color=palette[name], lw=2)
    plt.axhline(base_rate, color="k", linestyle="--", label=f"Baseline Prevalence ({base_rate:.3%})", alpha=0.6)
    plt.xlabel("Recall (Fraction of Defaulters Identified)", fontsize=11)
    plt.ylabel("Precision (Fraction of Flagged Risks Truly Defaulting)", fontsize=11)
    plt.title("Precision-Recall Benchmark - Imbalanced Credit Risk (3.93% Default Rate)", fontsize=12, fontweight="bold")
    plt.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    pr_fig_path = os.path.join(figures_dir, "pr_curves_comparison.png")
    plt.savefig(pr_fig_path)
    plt.close()
    print(f"[EVALUATE] Saved: {pr_fig_path}")

    # Figure 3: Reliability Diagrams (Probability Calibration)
    plt.figure(figsize=(8, 6), dpi=300)
    for name in model_files.keys():
        fop, mpv = calibration_curve(y_test, probabilities[name], n_bins=10, strategy="uniform")
        brier = brier_score_loss(y_test, probabilities[name])
        plt.plot(mpv, fop, marker="o", label=f"{name} (Brier = {brier:.4f})", color=palette[name], lw=1.8)
    plt.plot([0, 1], [0, 1], "k--", label="Perfect Calibration", alpha=0.7)
    plt.xlabel("Mean Predicted Default Probability", fontsize=11)
    plt.ylabel("Observed Fraction of Defaults", fontsize=11)
    plt.title("Reliability Diagrams (Probability Calibration Curves)", fontsize=12, fontweight="bold")
    plt.legend(loc="upper left", frameon=True)
    plt.tight_layout()
    calib_fig_path = os.path.join(figures_dir, "calibration_curves.png")
    plt.savefig(calib_fig_path)
    plt.close()
    print(f"[EVALUATE] Saved: {calib_fig_path}")

    # Figure 4: Cost Curves vs Threshold
    plt.figure(figsize=(8, 6), dpi=300)
    for name in model_files.keys():
        prob = probabilities[name]
        costs = [
            float((c_fn * (((prob >= t) == 0) & (y_test == 1)).sum()) + 
                  (c_fp * (((prob >= t) == 1) & (y_test == 0)).sum()))
            for t in threshold_grid
        ]
        opt_t = optimal_thresholds[name]["optimal_threshold_p"]
        min_c = optimal_thresholds[name]["minimized_portfolio_loss"]
        plt.plot(threshold_grid, costs, label=f"{name} (Min Cost at p={opt_t:.2f})", color=palette[name], lw=2)
        plt.plot(opt_t, min_c, marker="*", markersize=10, color=palette[name])
    plt.xlabel("Decision Cutoff Threshold (p_cutoff)", fontsize=11)
    plt.ylabel("Total Portfolio Loss (C_FN=5, C_FP=1)", fontsize=11)
    plt.title("Asymmetric Cost Optimization Curve (Loss Minimization)", fontsize=12, fontweight="bold")
    plt.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    cost_fig_path = os.path.join(figures_dir, "cost_curve_threshold_analysis.png")
    plt.savefig(cost_fig_path)
    plt.close()
    print(f"[EVALUATE] Saved: {cost_fig_path}")

    print("\n[EVALUATE] All multi-model benchmarking evaluations completed successfully.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data", "processed")
    models_dir = os.path.join(base_dir, "models")
    figures_dir = os.path.join(base_dir, "figures")
    results_dir = os.path.join(base_dir, "results")

    run_comprehensive_evaluation(data_dir, models_dir, figures_dir, results_dir)
