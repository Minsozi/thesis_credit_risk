"""
feature_engineering.py
----------------------
Feature Engineering, Categorical Encoding, Numerical Normalization,
and Data Leakage-Free Train/Test Splitting.

Enforces strict separation of protected demographic attributes (for fairness
audits only) and fits all transformers strictly on the training partition.
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

RANDOM_SEED = 42


def engineer_and_prepare_features(cleaned_filepath: str, output_dir: str, random_state: int = RANDOM_SEED):
    print(f"[FEATURE ENGINEERING] Loading cleaned data from: {cleaned_filepath}")
    df = pd.read_csv(cleaned_filepath)

    # 1. Feature Engineering: Domain Indicators
    # Cash flow to loan requested
    df["cashflow_to_loan_ratio"] = df["net_disposable_cashflow"] / (df["loan_amount_requested"] + 1.0)

    # Airtime stability index (frequency scaled by inverse volatility)
    df["airtime_stability_index"] = df["airtime_recharge_frequency"] / (df["airtime_recharge_volatility"] + 1e-4)

    # Debt burden ratio
    df["debt_burden_ratio"] = df["loan_amount_requested"] / (df["monthly_revenue_estimated"] + 1.0)

    # Repayment discipline score
    df["repayment_discipline_score"] = np.maximum(
        0,
        df["number_of_previous_loans"] - (2 * df["number_of_late_payments"]) - (4 * df["historical_default_count"])
    )

    # 2. Strict Architectural Separation: Target, Protected Attributes, and Features
    target_col = "loan_default_flag"
    y = df[target_col].copy()

    # Protected attributes: EXCLUDED from training features X to comply with
    # Namibian Constitution Art. 10 (Equality) and prevent direct algorithmic discrimination.
    protected_cols = ["gender", "urban_rural", "location_region", "business_registration_status"]
    protected_df = df[["applicant_id"] + protected_cols].copy()

    # Identifier to drop
    drop_cols = ["applicant_id", target_col] + protected_cols
    X_raw = df.drop(columns=drop_cols)

    # 3. Categorical Feature Encoding (One-Hot Encoding)
    categorical_cols = ["business_type", "loan_purpose", "financial_record_availability"]
    X_encoded = pd.get_dummies(X_raw, columns=categorical_cols, drop_first=True, dtype=float)

    feature_names = list(X_encoded.columns)
    print(f"[FEATURE ENGINEERING] Total engineered candidate features: {len(feature_names)}")

    # 4. Stratified Train/Test Split (70% Train, 30% Test)
    # Split index-aligned across X, y, and protected_df
    X_train_df, X_test_df, y_train, y_test, prot_train, prot_test = train_test_split(
        X_encoded, y, protected_df, test_size=0.30, random_state=random_state, stratify=y
    )

    print(f"[FEATURE ENGINEERING] Training samples: {len(X_train_df)} (Default rate: {y_train.mean():.3%})")
    print(f"[FEATURE ENGINEERING] Testing samples:  {len(X_test_df)} (Default rate: {y_test.mean():.3%})")

    # 5. Numerical Normalization (StandardScaler)
    # CRITICAL: Fit ONLY on training set to eliminate any data leakage
    scaler = StandardScaler()
    scaler.fit(X_train_df)

    X_train_scaled = pd.DataFrame(scaler.transform(X_train_df), columns=feature_names, index=X_train_df.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test_df), columns=feature_names, index=X_test_df.index)

    # 6. Save Processed Artifacts
    os.makedirs(output_dir, exist_ok=True)

    train_feat_path = os.path.join(output_dir, "train_features.csv")
    test_feat_path = os.path.join(output_dir, "test_features.csv")
    train_target_path = os.path.join(output_dir, "train_target.csv")
    test_target_path = os.path.join(output_dir, "test_target.csv")
    prot_test_path = os.path.join(output_dir, "protected_attributes_test.csv")
    meta_path = os.path.join(output_dir, "feature_metadata.json")

    X_train_scaled.to_csv(train_feat_path, index=False)
    X_test_scaled.to_csv(test_feat_path, index=False)
    y_train.to_csv(train_target_path, index=False)
    y_test.to_csv(test_target_path, index=False)
    prot_test.to_csv(prot_test_path, index=False)

    metadata = {
        "random_seed": random_state,
        "n_train": len(X_train_scaled),
        "n_test": len(X_test_scaled),
        "n_features": len(feature_names),
        "feature_names": feature_names,
        "categorical_columns_encoded": categorical_cols,
        "protected_attributes_held_out": protected_cols,
        "train_default_prevalence": float(y_train.mean()),
        "test_default_prevalence": float(y_test.mean())
    }

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    print(f"[FEATURE ENGINEERING] Processed train features saved to: {train_feat_path}")
    print(f"[FEATURE ENGINEERING] Processed test features saved to:  {test_feat_path}")
    print(f"[FEATURE ENGINEERING] Protected test attributes saved to: {prot_test_path}")
    print(f"[FEATURE ENGINEERING] Feature metadata saved to:        {meta_path}")

    return X_train_scaled, X_test_scaled, y_train, y_test, prot_test


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    cleaned_data = os.path.join(base_dir, "data", "processed", "cleaned_cohort.csv")
    proc_dir = os.path.join(base_dir, "data", "processed")
    
    engineer_and_prepare_features(cleaned_data, proc_dir)
