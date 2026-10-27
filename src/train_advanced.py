"""
train_advanced.py
-----------------
Training, 5-Fold Stratified Cross-Validation, Hyperparameter Tuning,
and Multi-Metric Evaluation for Advanced Ensemble Classifiers:
  3. Random Forest (Bagging Ensemble Standard; Breiman, 2001)
  4. XGBoost (Extreme Gradient Boosting Standard; Chen & Guestrin, 2016)

Evaluates full metric suite on the holdout test set: Accuracy, Precision,
Recall, F1, ROC-AUC, PR-AUC, Confusion Matrix, FPR, FNR, and Brier Score.
All random seeds set to 42 for academic reproducibility.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    confusion_matrix,
    brier_score_loss
)
from xgboost import XGBClassifier

RANDOM_SEED = 42


def evaluate_model_performance(y_true, y_pred, y_prob):
    """Computes full suite of credit risk metrics."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    roc_auc = roc_auc_score(y_true, y_prob)
    pr_auc = average_precision_score(y_true, y_prob)
    brier = brier_score_loss(y_true, y_prob)
    
    fpr = float(fp / (fp + tn)) if (fp + tn) > 0 else 0.0
    fnr = float(fn / (fn + tp)) if (fn + tp) > 0 else 0.0
    
    return {
        "accuracy": round(float(acc), 4),
        "precision": round(float(prec), 4),
        "recall_sensitivity": round(float(rec), 4),
        "f1_score": round(float(f1), 4),
        "roc_auc": round(float(roc_auc), 4),
        "pr_auc": round(float(pr_auc), 4),
        "brier_score_calibration": round(float(brier), 4),
        "false_positive_rate": round(float(fpr), 4),
        "false_negative_rate": round(float(fnr), 4),
        "confusion_matrix": {
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp)
        }
    }


def train_and_benchmark_advanced(data_dir: str, models_dir: str, results_dir: str):
    print("[ADVANCED TRAINING] Loading processed data...")
    X_train = pd.read_csv(os.path.join(data_dir, "train_features.csv"))
    y_train = pd.read_csv(os.path.join(data_dir, "train_target.csv")).squeeze()
    X_test = pd.read_csv(os.path.join(data_dir, "test_features.csv"))
    y_test = pd.read_csv(os.path.join(data_dir, "test_target.csv")).squeeze()

    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_SEED)

    # Calculate class imbalance ratio for XGBoost scale_pos_weight
    n_neg = (y_train == 0).sum()
    n_pos = (y_train == 1).sum()
    scale_pos = round(float(n_neg / n_pos), 2)
    print(f"[ADVANCED TRAINING] Imbalance ratio: {scale_pos}:1 (scale_pos_weight)")

    # -------------------------------------------------------------
    # 1. Advanced Model 3: Random Forest (Bagging Ensemble Standard)
    # -------------------------------------------------------------
    print("\n--- Training Model 3: Random Forest Classifier ---")
    rf_param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [6, 8, 12],
        "min_samples_leaf": [5, 10, 20],
        "max_features": ["sqrt"],
        "class_weight": ["balanced"]
    }

    rf_base = RandomForestClassifier(random_state=RANDOM_SEED, n_jobs=-1)
    rf_grid = GridSearchCV(rf_base, rf_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)
    rf_grid.fit(X_train, y_train)

    best_rf = rf_grid.best_estimator_
    print(f"[RANDOM FOREST] Best Parameters: {rf_grid.best_params_}")
    print(f"[RANDOM FOREST] Mean 5-Fold CV ROC-AUC: {rf_grid.best_score_:.4f}")

    # Holdout Test Evaluation
    rf_probs = best_rf.predict_proba(X_test)[:, 1]
    rf_preds = best_rf.predict(X_test)
    rf_test_metrics = evaluate_model_performance(y_test, rf_preds, rf_probs)

    rf_model_path = os.path.join(models_dir, "advanced_random_forest.joblib")
    joblib.dump(best_rf, rf_model_path)
    print(f"[RANDOM FOREST] Model saved to: {rf_model_path}")

    # -------------------------------------------------------------
    # 2. Advanced Model 4: XGBoost (Gradient Boosting Standard)
    # -------------------------------------------------------------
    print("\n--- Training Model 4: XGBoost Classifier ---")
    xgb_param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [3, 4, 5],
        "learning_rate": [0.03, 0.05, 0.1],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
        "scale_pos_weight": [scale_pos],
        "reg_lambda": [1.0, 5.0]
    }

    xgb_base = XGBClassifier(
        eval_metric="logloss",
        random_state=RANDOM_SEED,
        n_jobs=-1
    )
    xgb_grid = GridSearchCV(xgb_base, xgb_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)
    xgb_grid.fit(X_train, y_train)

    best_xgb = xgb_grid.best_estimator_
    print(f"[XGBOOST] Best Parameters: {xgb_grid.best_params_}")
    print(f"[XGBOOST] Mean 5-Fold CV ROC-AUC: {xgb_grid.best_score_:.4f}")

    # Holdout Test Evaluation
    xgb_probs = best_xgb.predict_proba(X_test)[:, 1]
    xgb_preds = best_xgb.predict(X_test)
    xgb_test_metrics = evaluate_model_performance(y_test, xgb_preds, xgb_probs)

    xgb_model_path = os.path.join(models_dir, "advanced_xgboost.joblib")
    joblib.dump(best_xgb, xgb_model_path)
    print(f"[XGBOOST] Model saved to: {xgb_model_path}")

    # -------------------------------------------------------------
    # 3. Export Metrics JSON
    # -------------------------------------------------------------
    advanced_results = {
        "metadata": {
            "random_seed": RANDOM_SEED,
            "cv_folds": 5,
            "scale_pos_weight": scale_pos,
            "n_train": len(X_train),
            "n_test": len(X_test),
            "test_default_count": int(y_test.sum()),
            "test_non_default_count": int((y_test == 0).sum())
        },
        "random_forest": {
            "best_hyperparameters": rf_grid.best_params_,
            "cv_mean_roc_auc": round(float(rf_grid.best_score_), 4),
            "holdout_test_metrics": rf_test_metrics
        },
        "xgboost": {
            "best_hyperparameters": xgb_grid.best_params_,
            "cv_mean_roc_auc": round(float(xgb_grid.best_score_), 4),
            "holdout_test_metrics": xgb_test_metrics
        }
    }

    results_path = os.path.join(results_dir, "advanced_models_metrics.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(advanced_results, f, indent=4)
    print(f"\n[ADVANCED BENCHMARK] Full metrics written to: {results_path}")

    # Print summary table
    print("\n" + "="*80)
    print(f"{'Metric':<28} | {'Random Forest':<22} | {'XGBoost':<20}")
    print("="*80)
    for m in ["roc_auc", "pr_auc", "recall_sensitivity", "false_negative_rate", "false_positive_rate", "f1_score", "accuracy", "brier_score_calibration"]:
        rf_v = rf_test_metrics[m]
        xgb_v = xgb_test_metrics[m]
        print(f"{m:<28} | {rf_v:<22} | {xgb_v:<20}")
    print("="*80)

    return advanced_results


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data", "processed")
    models_dir = os.path.join(base_dir, "models")
    results_dir = os.path.join(base_dir, "results")

    train_and_benchmark_advanced(data_dir, models_dir, results_dir)
