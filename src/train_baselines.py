"""
train_baselines.py
------------------
Training, Cross-Validation, Hyperparameter Tuning, and Multi-Metric
Benchmarking for Baseline Models:
  1. Logistic Regression (Linear Scorecard Standard)
  2. Decision Tree Classifier (Interpretable Rule-Based Standard)

Calculates complete metric suite: Accuracy, Precision, Recall, F1,
ROC-AUC, PR-AUC, Confusion Matrix, FPR, FNR, and Brier Score Calibration.
All random seeds explicitly set to 42 for academic reproducibility.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
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


def train_and_benchmark_baselines(data_dir: str, models_dir: str, results_dir: str):
    print("[BASELINE TRAINING] Loading processed data...")
    X_train = pd.read_csv(os.path.join(data_dir, "train_features.csv"))
    y_train = pd.read_csv(os.path.join(data_dir, "train_target.csv")).squeeze()
    X_test = pd.read_csv(os.path.join(data_dir, "test_features.csv"))
    y_test = pd.read_csv(os.path.join(data_dir, "test_target.csv")).squeeze()

    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    results = {}
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_SEED)

    # -------------------------------------------------------------
    # 1. Baseline 1: Logistic Regression (Linear Scorecard Standard)
    # -------------------------------------------------------------
    print("\n--- Training Model 1: Logistic Regression ---")
    lr_param_grid = {
        "C": [0.01, 0.05, 0.1, 0.5, 1.0, 5.0],
        "penalty": ["l2"],
        "solver": ["lbfgs"],
        "class_weight": ["balanced"]  # Addresses 3.94% default imbalance
    }

    lr_base = LogisticRegression(max_iter=1000, random_state=RANDOM_SEED)
    lr_grid = GridSearchCV(lr_base, lr_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)
    lr_grid.fit(X_train, y_train)

    best_lr = lr_grid.best_estimator_
    print(f"[LOGISTIC REGRESSION] Best Parameters: {lr_grid.best_params_}")
    print(f"[LOGISTIC REGRESSION] Mean 5-Fold CV ROC-AUC: {lr_grid.best_score_:.4f}")

    # Evaluate on Holdout Test Set
    lr_probs = best_lr.predict_proba(X_test)[:, 1]
    # Standard 0.5 cutoff
    lr_preds_default = best_lr.predict(X_test)
    # Calibrated risk cutoff (p_cutoff = 0.5 on balanced model aligns with cost ratio)
    lr_test_metrics = evaluate_model_performance(y_test, lr_preds_default, lr_probs)

    # Save model artifact
    lr_model_path = os.path.join(models_dir, "baseline_logistic_regression.joblib")
    joblib.dump(best_lr, lr_model_path)
    print(f"[LOGISTIC REGRESSION] Model saved to: {lr_model_path}")

    # -------------------------------------------------------------
    # 2. Baseline 2: Decision Tree (Interpretable Rule-Based Standard)
    # -------------------------------------------------------------
    print("\n--- Training Model 2: Decision Tree Classifier ---")
    dt_param_grid = {
        "max_depth": [3, 4, 5, 6],
        "min_samples_leaf": [15, 25, 40, 60],
        "criterion": ["gini", "entropy"],
        "class_weight": ["balanced"]
    }

    dt_base = DecisionTreeClassifier(random_state=RANDOM_SEED)
    dt_grid = GridSearchCV(dt_base, dt_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)
    dt_grid.fit(X_train, y_train)

    best_dt = dt_grid.best_estimator_
    print(f"[DECISION TREE] Best Parameters: {dt_grid.best_params_}")
    print(f"[DECISION TREE] Mean 5-Fold CV ROC-AUC: {dt_grid.best_score_:.4f}")

    # Evaluate on Holdout Test Set
    dt_probs = best_dt.predict_proba(X_test)[:, 1]
    dt_preds_default = best_dt.predict(X_test)
    dt_test_metrics = evaluate_model_performance(y_test, dt_preds_default, dt_probs)

    # Save model artifact
    dt_model_path = os.path.join(models_dir, "baseline_decision_tree.joblib")
    joblib.dump(best_dt, dt_model_path)
    print(f"[DECISION TREE] Model saved to: {dt_model_path}")

    # -------------------------------------------------------------
    # 3. Compile & Export Benchmark Results
    # -------------------------------------------------------------
    results = {
        "metadata": {
            "random_seed": RANDOM_SEED,
            "cv_folds": 5,
            "n_train": len(X_train),
            "n_test": len(X_test),
            "test_default_count": int(y_test.sum()),
            "test_non_default_count": int((y_test == 0).sum())
        },
        "logistic_regression": {
            "best_hyperparameters": lr_grid.best_params_,
            "cv_mean_roc_auc": round(float(lr_grid.best_score_), 4),
            "holdout_test_metrics": lr_test_metrics
        },
        "decision_tree": {
            "best_hyperparameters": dt_grid.best_params_,
            "cv_mean_roc_auc": round(float(dt_grid.best_score_), 4),
            "holdout_test_metrics": dt_test_metrics
        }
    }

    results_path = os.path.join(results_dir, "baseline_models_metrics.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"\n[BASELINE BENCHMARK] Full evaluation metrics written to: {results_path}")

    # Print summary comparative table
    print("\n" + "="*80)
    print(f"{'Metric':<28} | {'Logistic Regression':<22} | {'Decision Tree':<20}")
    print("="*80)
    for metric_name in ["roc_auc", "pr_auc", "recall_sensitivity", "false_negative_rate", "false_positive_rate", "f1_score", "accuracy", "brier_score_calibration"]:
        lr_val = lr_test_metrics[metric_name]
        dt_val = dt_test_metrics[metric_name]
        print(f"{metric_name:<28} | {lr_val:<22} | {dt_val:<20}")
    print("="*80)

    return results


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data", "processed")
    models_dir = os.path.join(base_dir, "models")
    results_dir = os.path.join(base_dir, "results")

    train_and_benchmark_baselines(data_dir, models_dir, results_dir)
