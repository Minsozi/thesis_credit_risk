"""
explainability.py
-----------------
Explainable AI (XAI) Implementation for Credit Risk Models:
  1. TreeSHAP Global Feature Importance
  2. SHAP Summary Beeswarm Plot
  3. SHAP Partial Dependence Analysis
  4. Local Adverse-Action Reason Code Generation (Bank of Namibia Compliance)

Provides transparent, interpretable risk attributions meeting the disclosure
standards of the Bank of Namibia Revised Fintech Innovation Framework 2026.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap

RANDOM_SEED = 42


def run_explainability_pipeline(data_dir: str, models_dir: str, figures_dir: str, results_dir: str):
    print("[EXPLAINABILITY] Loading test data and trained models...")
    X_test = pd.read_csv(os.path.join(data_dir, "test_features.csv"))
    y_test = pd.read_csv(os.path.join(data_dir, "test_target.csv")).squeeze().values
    prot_test = pd.read_csv(os.path.join(data_dir, "protected_attributes_test.csv"))

    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    xgb_model_path = os.path.join(models_dir, "advanced_xgboost.joblib")
    best_xgb = joblib.load(xgb_model_path)
    print("[EXPLAINABILITY] Loaded XGBoost model for TreeSHAP analysis.")

    # -------------------------------------------------------------
    # 1. Compute TreeSHAP Values
    # -------------------------------------------------------------
    print("[EXPLAINABILITY] Computing TreeSHAP values for 1,500 test instances...")
    explainer = shap.TreeExplainer(best_xgb)
    shap_values = explainer(X_test)
    shap_vals_arr = shap_values.values  # Shape: (1500, 35)

    # -------------------------------------------------------------
    # 2. Global Feature Importance Ranking
    # -------------------------------------------------------------
    mean_abs_shap = np.mean(np.abs(shap_vals_arr), axis=0)
    feature_names = list(X_test.columns)

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Mean_Absolute_SHAP": mean_abs_shap
    }).sort_values(by="Mean_Absolute_SHAP", ascending=False).reset_index(drop=True)

    importance_path = os.path.join(results_dir, "shap_feature_importance.csv")
    importance_df.to_csv(importance_path, index=False)
    print(f"[EXPLAINABILITY] Global feature importance exported to: {importance_path}")

    print("\n--- Top 10 Most Influential Credit Risk Features (Global SHAP) ---")
    print(importance_df.head(10).to_string(index=False))

    # -------------------------------------------------------------
    # 3. Publication Figures Generation
    # -------------------------------------------------------------
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Figure 1: Global Mean Absolute SHAP Bar Chart
    plt.figure(figsize=(10, 6), dpi=300)
    top15 = importance_df.head(15).iloc[::-1]
    plt.barh(top15["Feature"], top15["Mean_Absolute_SHAP"], color="#1f77b4", edgecolor="none", height=0.7)
    plt.xlabel("Mean |SHAP Value| (Average Impact on Log-Odds Default Risk)", fontsize=11)
    plt.title("Global Feature Importance - TreeSHAP (Top 15 Predictors)", fontsize=12, fontweight="bold")
    plt.tight_layout()
    bar_fig_path = os.path.join(figures_dir, "shap_feature_importance_bar.png")
    plt.savefig(bar_fig_path)
    plt.close()
    print(f"[EXPLAINABILITY] Saved: {bar_fig_path}")

    # Figure 2: SHAP Summary Beeswarm Plot
    plt.figure(figsize=(11, 7), dpi=300)
    shap.summary_plot(shap_vals_arr, X_test, max_display=15, show=False)
    plt.title("SHAP Beeswarm Summary Plot: Feature Magnitude & Risk Directionality", fontsize=12, fontweight="bold", pad=15)
    plt.tight_layout()
    beeswarm_fig_path = os.path.join(figures_dir, "shap_summary_beeswarm.png")
    plt.savefig(beeswarm_fig_path, bbox_inches="tight")
    plt.close()
    print(f"[EXPLAINABILITY] Saved: {beeswarm_fig_path}")

    # Figure 3: Partial Dependence Analysis (4-Panel Grid)
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), dpi=300)
    key_features = [
        "installment_to_income_ratio",
        "airtime_recharge_volatility",
        "cashflow_to_loan_ratio",
        "repayment_discipline_score"
    ]
    titles = [
        "(A) Installment-to-Income Ratio vs. Risk Impact",
        "(B) Airtime Recharge Volatility vs. Risk Impact",
        "(C) Cashflow-to-Loan Ratio vs. Risk Impact",
        "(D) Repayment Discipline Score vs. Risk Impact"
    ]

    for ax, feat, title in zip(axes.flatten(), key_features, titles):
        if feat in X_test.columns:
            feat_idx = X_test.columns.get_loc(feat)
            x_vals = X_test[feat].values
            s_vals = shap_vals_arr[:, feat_idx]
            # Scatter with smooth trend
            ax.scatter(x_vals, s_vals, alpha=0.35, color="#2b5c8f", s=18)
            # Lowess or polynomial trendline
            z = np.polyfit(x_vals, s_vals, 3)
            p = np.poly1d(z)
            x_sorted = np.sort(x_vals)
            ax.plot(x_sorted, p(x_sorted), color="#d62728", lw=2.2, label="Non-linear Trend")
            ax.axhline(0, color="k", linestyle="--", alpha=0.5)
            ax.set_xlabel(f"{feat} (Standardized)", fontsize=10)
            ax.set_ylabel("SHAP Value (Impact on Default Risk)", fontsize=10)
            ax.set_title(title, fontsize=11, fontweight="bold")
            ax.legend(loc="best")
            ax.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    dep_fig_path = os.path.join(figures_dir, "shap_dependence_plots.png")
    plt.savefig(dep_fig_path)
    plt.close()
    print(f"[EXPLAINABILITY] Saved: {dep_fig_path}")

    # -------------------------------------------------------------
    # 4. Local Adverse-Action Reason Codes (Bank of Namibia Compliance)
    # -------------------------------------------------------------
    # Human-readable dictionary mapping feature names to plain-language disclosures
    reason_translations = {
        "installment_to_income_ratio": "Monthly installment exceeds recommended proportion of free cash flow.",
        "airtime_recharge_volatility": "High variability in monthly mobile airtime recharge amounts indicates irregular disposable income.",
        "cashflow_to_loan_ratio": "Net disposable monthly cash flow is insufficient to absorb unexpected liquidity shocks.",
        "repayment_discipline_score": "Elevated count of late payments or previous facility delinquencies.",
        "debt_burden_ratio": "Requested loan amount is high relative to estimated monthly business revenue.",
        "mobile_wallet_txn_regularity": "Low consistency in mobile wallet transaction activity.",
        "airtime_recharge_frequency": "Low frequency of mobile top-up transactions over the preceding 90 days.",
        "utility_payment_missing_flag": "No verified municipal utility billing track record on file.",
        "number_of_late_payments": "Past late repayment history on digital or microfinance credit facilities.",
        "historical_default_count": "Previous un-remedied default on digital credit facilities.",
        "account_age_telecom": "Mobile SIM / wallet account has a relatively short operating history.",
        "savings_deposit_frequency": "Infrequent micro-savings or fund replenishment deposits."
    }

    test_probs = best_xgb.predict_proba(X_test)[:, 1]
    
    # Identify exemplary cases:
    # Case 1: Approved Applicant (Low Risk, actual non-default)
    approved_indices = np.where((test_probs < 0.20) & (y_test == 0))[0]
    case_approved_idx = int(approved_indices[0]) if len(approved_indices) > 0 else 0

    # Case 2: Declined Applicant (High Risk, actual default or predicted high risk)
    declined_indices = np.where((test_probs > 0.60))[0]
    case_declined_idx = int(declined_indices[0]) if len(declined_indices) > 0 else 1

    case_studies = {}
    for case_type, idx in [("Approved_Applicant_Case", case_approved_idx), ("Declined_Applicant_Case", case_declined_idx)]:
        applicant_id = prot_test.iloc[idx]["applicant_id"]
        prob_val = float(test_probs[idx])
        actual_label = int(y_test[idx])
        
        row_shap = shap_vals_arr[idx]
        top_risk_drivers = np.argsort(row_shap)[::-1][:3]
        top_protective_factors = np.argsort(row_shap)[:3]

        adverse_reasons = []
        for feat_i in top_risk_drivers:
            feat_name = feature_names[feat_i]
            impact = float(row_shap[feat_i])
            if impact > 0:
                explanation = reason_translations.get(feat_name, f"Adverse risk impact from {feat_name}.")
                adverse_reasons.append({
                    "feature": feat_name,
                    "shap_impact": round(impact, 4),
                    "regulatory_reason_code": explanation
                })

        protective_reasons = []
        for feat_i in top_protective_factors:
            feat_name = feature_names[feat_i]
            impact = float(row_shap[feat_i])
            if impact < 0:
                protective_reasons.append({
                    "feature": feat_name,
                    "shap_impact": round(impact, 4),
                    "protective_factor": f"Favorable indicator reducing default probability ({feat_name})."
                })

        case_studies[case_type] = {
            "applicant_id": applicant_id,
            "test_sample_index": idx,
            "predicted_default_probability": round(prob_val, 4),
            "credit_decision": "Approved" if prob_val < 0.594 else "Declined (Adverse Action Notice Generated)",
            "ground_truth_outcome": "Non-Default (Good)" if actual_label == 0 else "Default (Bad)",
            "adverse_action_disclosures": adverse_reasons,
            "favorable_mitigating_factors": protective_reasons,
            "protected_profile_audit": {
                "gender": prot_test.iloc[idx]["gender"],
                "urban_rural": prot_test.iloc[idx]["urban_rural"],
                "location_region": prot_test.iloc[idx]["location_region"]
            }
        }

    cases_path = os.path.join(results_dir, "local_adverse_action_explanations.json")
    with open(cases_path, "w", encoding="utf-8") as f:
        json.dump(case_studies, f, indent=4)
    print(f"[EXPLAINABILITY] Local adverse action case studies exported to: {cases_path}")

    # Figure 4: Individual Waterfall Plot for the Declined Applicant
    plt.figure(figsize=(10, 5), dpi=300)
    # Generate waterfall explanation object
    shap.plots.waterfall(shap_values[case_declined_idx], max_display=10, show=False)
    plt.title(f"Individual Adverse-Action Explanation: Declined Applicant ({prot_test.iloc[case_declined_idx]['applicant_id']})", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout()
    waterfall_path = os.path.join(figures_dir, "individual_adverse_action_waterfall.png")
    plt.savefig(waterfall_path, bbox_inches="tight")
    plt.close()
    print(f"[EXPLAINABILITY] Saved: {waterfall_path}")

    print("[EXPLAINABILITY] TreeSHAP and explainability pipeline completed successfully.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data", "processed")
    models_dir = os.path.join(base_dir, "models")
    figures_dir = os.path.join(base_dir, "figures")
    results_dir = os.path.join(base_dir, "results")

    run_explainability_pipeline(data_dir, models_dir, figures_dir, results_dir)
