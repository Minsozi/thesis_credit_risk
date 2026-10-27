# Stage 8: Baseline Machine Learning Models Specification & Evaluation

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** Logistic Regression (Linear Scorecard Standard) vs. Decision Tree (Rule-Based Standard)  

---

## 1. Executive Summary

In accordance with Section 10 of the thesis development guidelines, this report evaluates the baseline machine learning classifiers on the processed alternative-data credit dataset ($N_{\text{train}} = 3,500$, $N_{\text{test}} = 1,500$; empirical default prevalence $3.94\%$).

The two investigated baseline models represent the foundational standards of consumer credit scoring:
1. **Logistic Regression:** The classical industry scorecard standard (Thomas et al., 2002; Lessmann et al., 2015), representing a parametric linear log-odds decision boundary.
2. **Decision Tree Classifier (CART):** The non-parametric, rule-based interpretable benchmark (Breiman et al., 1984), generating hierarchical split criteria without modeling interactions as smooth functions.

Both models were trained using **5-fold stratified cross-validation** with hyperparameter tuning on the training set, and subsequently evaluated on the **completely untouched 1,500-observation holdout test set**.

---

## 2. Model Architectures & Tuned Hyperparameters

| Hyperparameter / Dimension | Logistic Regression (Scorecard Standard) | Decision Tree (Rule-Based Benchmark) | Rationale & Methodology |
| :--- | :--- | :--- | :--- |
| **Model Type** | `sklearn.linear_model.LogisticRegression` | `sklearn.tree.DecisionTreeClassifier` | Standard scikit-learn implementations |
| **Class Weighting** | `class_weight='balanced'` | `class_weight='balanced'` | Adjusts loss weights inversely proportional to class frequencies to handle $3.94\%$ default sparsity |
| **Regularization / Pruning** | $L_2$ Penalty ($C = 0.01$) | Max Depth = 5, Min Leaf = 40 | Grid-searched to minimize overfitting on training folds |
| **Split / Solver Criterion** | L-BFGS Quasi-Newton Optimizer | Information Gain (`criterion='entropy'`) | Optimizes classification log-loss and node purity |
| **Mean 5-Fold CV ROC-AUC** | **$0.7325 \pm 0.024$** | **$0.6361 \pm 0.038$** | Cross-validated on training partition |
| **Serialized Model File** | `models/baseline_logistic_regression.joblib` | `models/baseline_decision_tree.joblib` | Stored for reproducibility |

---

## 3. Comparative Holdout Test Performance (results/baseline_models_metrics.json)

The models were evaluated on the independent holdout testing set ($1,500$ records: $59$ actual defaults, $1,441$ non-defaults).

```
========================================================================================
Evaluation Metric            | Logistic Regression (L2) | Decision Tree (CART) | Benchmark Goal
========================================================================================
ROC-AUC                      | 0.6668                   | 0.5425               | Higher is better
PR-AUC (Average Precision)   | 0.1459                   | 0.0459               | Baseline prevalence = 0.0393
Recall / Sensitivity         | 0.5254                   | 0.4068               | Detect actual defaulters
False Negative Rate (FNR)    | 0.4746                   | 0.5932               | Lower is critical (Credit Loss)
False Positive Rate (FPR)    | 0.3026                   | 0.3019               | Forgone creditworthy inclusion
F1-Score                     | 0.1179                   | 0.0927               | Harmonic balance
Classification Accuracy      | 0.6907                   | 0.6867               | Misleading under imbalance
Brier Score (Calibration)    | 0.2019                   | 0.2086               | Probability accuracy (0 = perfect)
========================================================================================
```

### Detailed Confusion Matrix Breakdown

```
Logistic Regression (Holdout Set, N = 1,500):
┌────────────────────────┬────────────────────────┐
│ True Negatives (TN):   │ False Positives (FP):  │
│ 1,005 (Safe Approved)  │ 436 (Safe Rejected)    │
├────────────────────────┼────────────────────────┤
│ False Negatives (FN):  │ True Positives (TP):   │
│ 28 (Default Missed)    │ 31 (Default Caught)    │
└────────────────────────┴────────────────────────┘

Decision Tree (Holdout Set, N = 1,500):
┌────────────────────────┬────────────────────────┐
│ True Negatives (TN):   │ False Positives (FP):  │
│ 1,006 (Safe Approved)  │ 435 (Safe Rejected)    │
├────────────────────────┼────────────────────────┤
│ False Negatives (FN):  │ True Positives (TP):   │
│ 35 (Default Missed)    │ 24 (Default Caught)    │
└────────────────────────┴────────────────────────┘
```

---

## 4. In-Depth Empirical Findings & Analysis

### 1. The Cost-Sensitive False Negative Crisis
* In credit risk modeling, the prompt template explicitly instructs: *"For credit-risk prediction, pay particular attention to false negatives because incorrectly classifying a risky applicant as low-risk can have serious consequences."*
* **Logistic Regression missed 28 out of 59 defaults ($FNR = 47.46\%$)**, while the **Decision Tree missed 35 out of 59 defaults ($FNR = 59.32\%$)**.
* In an operational microlending environment like *Tamba Maris*, missing half of all defaulting borrowers would rapidly erode the lending institution's capital adequacy ratio (CAR) and violate the Bank of Namibia's prudential safety guidelines.

### 2. Discrimination vs. Calibration (PR-AUC & Brier Score)
* While standard accuracy is approximately $69\%$ for both models, this is largely an artifact of correctly identifying non-defaulters ($TN = 1,005$).
* **PR-AUC (Precision-Recall Area Under Curve):** Logistic Regression achieved a PR-AUC of **$0.1459$**, representing a substantial 3.7x lift over the baseline random guessing rate ($3.93\%$), but leaving substantial room for improvement. The Decision Tree achieved a PR-AUC of only **$0.0459$**, barely above random chance.
* **Brier Score:** Both models achieved Brier scores around **$0.20$** ($0.2019$ and $0.2086$), indicating that while their ranked order is partially informative, their uncalibrated output probabilities deviate from true default likelihoods due to balanced class weighting.

### 3. Why Linear & Single Tree Models Fail on Alternative Data
* Alternative data features (such as airtime recharge volatility, mobile wallet transaction regularity, and net cash flow) do not operate independently. Their predictive signal is driven by **non-linear threshold interactions** (e.g., high recharge volatility is harmless if cash flow is high, but fatal if debt burden exceeds 30%).
* A linear model cannot capture these multi-way interactions without manual polynomial expansion, while a single pruned decision tree suffers from high variance and step-function approximations.
* **Conclusion:** This empirical finding directly validates the theoretical motivation for **Ensemble Learning (Hypothesis $H_{1,2}$)**.

---

## 5. Next Steps & Transition to Stage 9

With baseline lower bounds empirically established and serialized, the next operational milestone is:
> **STAGE 9: Build and tune advanced models**  
> Implement, tune, and evaluate **Random Forest** (bagging ensemble) and **XGBoost** (extreme gradient boosting) to capture high-dimensional non-linear interactions, lower the False Negative Rate ($FNR$), and elevate PR-AUC and ROC-AUC.
