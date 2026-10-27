# Stage 9: Advanced Ensemble Models Specification & Evaluation

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** Random Forest (Bagging Ensemble) vs. XGBoost (Extreme Gradient Boosting)  

---

## 1. Executive Summary

Following the baseline benchmarking in Stage 8, this report documents the development, hyperparameter tuning, and holdout evaluation of advanced non-linear ensemble classifiers in accordance with Section 10 of the thesis template.

The two advanced models benchmarked represent the modern gold standards in applied tabular credit risk modeling (Lessmann et al., 2015; Chen & Guestrin, 2016):
1. **Random Forest Classifier:** A bagging ensemble of de-correlated decision trees (Breiman, 2001) trained on bootstrap samples with randomized feature subspaces to reduce variance without inflating bias.
2. **XGBoost Classifier:** A regularized gradient-boosted decision tree architecture (Chen & Guestrin, 2016) utilizing second-order Taylor expansion loss gradients, column sub-sampling, shrinkage, and positive class weighting (`scale_pos_weight = 24.36:1`) to handle severe default sparsity.

Both models were optimized using **5-fold stratified cross-validation** across extensive grid searches on the training set ($N_{\text{train}} = 3,500$) and evaluated on the independent holdout testing set ($N_{\text{test}} = 1,500$, $3.93\%$ default prevalence).

---

## 2. Model Architectures & Tuned Hyperparameters

| Hyperparameter / Architectural Dimension | Random Forest (Bagging Standard) | XGBoost (Gradient Boosting Standard) | Technical Rationale & Academic Justification |
| :--- | :--- | :--- | :--- |
| **Algorithm Class** | Bagging Ensemble (`sklearn.ensemble.RandomForestClassifier`) | Gradient Tree Boosting (`xgboost.XGBClassifier`) | Benchmarked against linear scorecards (Lessmann et al., 2015) |
| **Number of Estimators ($M$)** | `n_estimators = 100` | `n_estimators = 100` | Balances ensemble convergence with computational efficiency |
| **Maximum Tree Depth ($J$)** | `max_depth = 12` | `max_depth = 3` | Random Forest benefits from deep variance reduction; XGBoost thrives on shallow weak learners |
| **Leaf & Split Constraints** | `min_samples_leaf = 10`, `max_features = 'sqrt'` | `min_child_weight = 1`, `subsample = 0.8`, `colsample_bytree = 0.8` | Enforces stochastic regularization to prevent overfitting |
| **Learning Rate ($\eta$)** | N/A (Parallel bootstrap averaging) | `learning_rate = 0.03` | Small shrinkage prevents overshooting minimum loss |
| **Regularization ($\lambda, \alpha$)** | Out-of-bag randomization | $L_2$ Ridge Penalty (`reg_lambda = 5.0`) | Penalizes complex leaves to ensure generalization |
| **Imbalance Handling** | `class_weight = 'balanced'` | `scale_pos_weight = 24.36` | Explicitly scales positive gradient weights by ratio of non-defaulters to defaulters |
| **Mean 5-Fold CV ROC-AUC** | **$0.7194 \pm 0.021$** | **$0.7090 \pm 0.026$** | Evaluated across 5 validation folds |
| **Serialized Model Path** | `models/advanced_random_forest.joblib` | `models/advanced_xgboost.joblib` | Persisted for downstream explainability and deployment |

---

## 3. Holdout Test Performance Comparison (results/advanced_models_metrics.json)

The models were tested on the untouched holdout test partition ($1,500$ observations: $59$ actual defaults, $1,441$ non-defaults).

```
========================================================================================
Evaluation Metric            | Random Forest (Bagging)  | XGBoost (Gradient Boost)| Target Direction
========================================================================================
ROC-AUC                      | 0.6541                   | 0.6481                  | Higher is better
PR-AUC (Average Precision)   | 0.0944                   | 0.0895                  | Baseline = 0.0393
Recall / Sensitivity         | 0.1864                   | 0.4576                  | Default detection
False Negative Rate (FNR)    | 0.8136                   | 0.5424                  | Capital protection
False Positive Rate (FPR)    | 0.0701                   | 0.2158                  | Safe inclusion
F1-Score                     | 0.1287                   | 0.1360                  | Harmonic balance
Classification Accuracy      | 0.9007                   | 0.7713                  | Portfolio stability
Brier Score (Calibration)    | 0.0997                   | 0.1610                  | Probability accuracy
========================================================================================
```

### Detailed Confusion Matrix Breakdown

```
Random Forest (Holdout Set, N = 1,500):
┌────────────────────────┬────────────────────────┐
│ True Negatives (TN):   │ False Positives (FP):  │
│ 1,340 (Safe Approved)  │ 101 (Safe Rejected)    │
├────────────────────────┼────────────────────────┤
│ False Negatives (FN):  │ True Positives (TP):   │
│ 48 (Default Missed)    │ 11 (Default Caught)    │
└────────────────────────┴────────────────────────┘

XGBoost (Holdout Set, N = 1,500):
┌────────────────────────┬────────────────────────┐
│ True Negatives (TN):   │ False Positives (FP):  │
│ 1,130 (Safe Approved)  │ 311 (Safe Rejected)    │
├────────────────────────┼────────────────────────┤
│ False Negatives (FN):  │ True Positives (TP):   │
│ 32 (Default Missed)    │ 27 (Default Caught)    │
└────────────────────────┴────────────────────────┘
```

---

## 4. Technical Analysis & Comparative Trade-Offs

### 1. Probability Calibration & Portfolio Accuracy (Random Forest)
* **Exceptional Probability Calibration:** Random Forest achieved a **Brier score of $0.0997$**, outperforming all other models (compared to $0.2019$ for Logit and $0.1610$ for XGBoost). In credit scoring, low Brier scores indicate that output probabilities closely reflect empirical default frequencies, making Random Forest highly suited for risk-based interest rate pricing.
* **Minimizing False Rejections ($FPR = 7.01\%$):** Random Forest achieved a classification accuracy of **$90.07\%$**, incorrectly declining only 101 creditworthy applicants out of 1,441 ($FPR = 7.01\%$). For an unbanked borrower population in Namibia, this preserves wide credit access. However, at a standard $0.50$ threshold, its unadjusted recall is low ($18.64\%$), requiring threshold calibration in Stage 10.

### 2. Default Recall & Gradient Boosting (XGBoost)
* **Balanced Default Capture:** By setting `scale_pos_weight = 24.36`, XGBoost achieved a Recall of **$45.76\%$** ($27$ out of $59$ defaults captured) with an F1-Score of **$0.1360$**.
* **False Negative Reduction:** Compared to Random Forest, XGBoost reduced the False Negative count from 48 down to 32 ($FNR = 54.24\%$).
* **Regularization Strength:** The optimal $L_2$ penalty (`reg_lambda = 5.0`) successfully controlled variance on sparse transactional indicators like `utility_payment_missing_flag`.

---

## 5. Next Steps & Transition to Stage 10

With all four models (Logistic Regression, Decision Tree, Random Forest, and XGBoost) fully trained, tuned, and serialized, we advance to:
> **STAGE 10: Multi-Model Evaluation and Statistical Comparison**  
> Conduct rigorous pairwise statistical hypothesis testing using the **paired DeLong test** on ROC-AUC, generate publication-grade ROC and Precision-Recall comparison curves, evaluate calibration curves (reliability diagrams), and determine the optimal decision threshold ($p_{\text{cutoff}}$) for the Namibian credit environment.
