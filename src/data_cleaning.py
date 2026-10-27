"""
data_cleaning.py
----------------
Data Profiling, Missing-Value Handling, Duplicate Detection,
and Outlier Investigation for the Credit Risk Dataset.

Performs reproducible cleaning and produces an audit trail report.
"""

import os
import json
import numpy as np
import pandas as pd


def profile_and_clean_data(raw_filepath: str, output_filepath: str, report_filepath: str) -> pd.DataFrame:
    print(f"[DATA CLEANING] Loading raw data from: {raw_filepath}")
    df = pd.read_csv(raw_filepath)
    n_initial = len(df)

    profiling_report = {
        "raw_record_count": n_initial,
        "initial_features_count": len(df.columns),
        "columns": list(df.columns)
    }

    # 1. Duplicate Detection
    duplicate_ids = df["applicant_id"].duplicated().sum()
    duplicate_rows = df.duplicated().sum()
    profiling_report["duplicate_ids"] = int(duplicate_ids)
    profiling_report["duplicate_rows"] = int(duplicate_rows)
    if duplicate_rows > 0:
        df = df.drop_duplicates().reset_index(drop=True)
        print(f"[DATA CLEANING] Dropped {duplicate_rows} exact duplicate rows.")

    # 2. Missing Value Analysis
    missing_summary = df.isnull().sum()
    missing_dict = {col: int(val) for col, val in missing_summary.items() if val > 0}
    profiling_report["missing_values"] = missing_dict
    print(f"[DATA CLEANING] Missing values detected: {missing_dict}")

    # 3. Informative Missingness Handling
    # Utility consistency missingness indicates unmetered / informal dwelling.
    if "utility_bill_payment_consistency" in df.columns:
        df["utility_payment_missing_flag"] = df["utility_bill_payment_consistency"].isnull().astype(int)
        median_utility = df["utility_bill_payment_consistency"].median()
        df["utility_bill_payment_consistency"] = df["utility_bill_payment_consistency"].fillna(median_utility)
        profiling_report["utility_missing_flag_created"] = True
        profiling_report["utility_imputed_median"] = float(median_utility)

    # Median imputation for any other numerical columns with missing values
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().sum() > 0:
            med_val = df[col].median()
            df[col] = df[col].fillna(med_val)

    # 4. Domain Range Validation & Integrity Checks
    invalid_age = (df["applicant_age"] < 18) | (df["applicant_age"] > 75)
    invalid_revenue = df["monthly_revenue_estimated"] < 0
    invalid_loan = df["loan_amount_requested"] <= 0
    profiling_report["range_violations"] = {
        "invalid_age_count": int(invalid_age.sum()),
        "invalid_revenue_count": int(invalid_revenue.sum()),
        "invalid_loan_amount_count": int(invalid_loan.sum())
    }

    # 5. Outlier Investigation & Winsorization (Clipping at 1st and 99th percentiles)
    skewed_numeric_cols = [
        "monthly_revenue_estimated",
        "monthly_operating_expenses",
        "net_disposable_cashflow",
        "p2p_transfer_in_out_ratio",
        "airtime_recharge_frequency"
    ]

    winsorization_bounds = {}
    for col in skewed_numeric_cols:
        if col in df.columns:
            q01 = df[col].quantile(0.01)
            q99 = df[col].quantile(0.99)
            winsorization_bounds[col] = {"p01": float(q01), "p99": float(q99)}
            df[col] = df[col].clip(lower=q01, upper=q99)

    profiling_report["winsorization_bounds"] = winsorization_bounds

    # 6. Class Imbalance Verification
    target_counts = df["loan_default_flag"].value_counts().to_dict()
    target_proportions = (df["loan_default_flag"].value_counts(normalize=True) * 100).round(2).to_dict()
    profiling_report["class_imbalance"] = {
        "counts": {str(k): int(v) for k, v in target_counts.items()},
        "proportions_pct": {str(k): float(v) for k, v in target_proportions.items()}
    }
    print(f"[DATA CLEANING] Class Distribution: {target_counts} ({target_proportions}%)")

    # 7. Save Cleaned Dataset & Audit Report
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    df.to_csv(output_filepath, index=False)
    print(f"[DATA CLEANING] Cleaned data successfully written to: {output_filepath}")

    os.makedirs(os.path.dirname(report_filepath), exist_ok=True)
    with open(report_filepath, "w", encoding="utf-8") as f:
        json.dump(profiling_report, f, indent=4)
    print(f"[DATA CLEANING] Profiling audit report written to: {report_filepath}")

    return df


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_path = os.path.join(base_dir, "data", "raw", "namibian_sandbox_cohort.csv")
    out_path = os.path.join(base_dir, "data", "processed", "cleaned_cohort.csv")
    rep_path = os.path.join(base_dir, "results", "data_profiling_report.json")
    
    profile_and_clean_data(raw_path, out_path, rep_path)
