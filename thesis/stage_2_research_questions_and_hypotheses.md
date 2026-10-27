# Stage 2: Research Questions & Testable Hypotheses

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Project:** Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia  

---

## 1. Overarching Primary Research Question

> **Primary Research Question (PRQ):**  
> *To what extent can machine learning models leveraging alternative transactional and behavioral data accurately, transparently, and fairly predict credit default risk for underserved, thin-file borrowers, and how can such a framework be responsibly operationalized within Namibia's evolving regulatory and financial sector environment?*

---

## 2. Secondary Research Questions (SRQs) & Testable Hypotheses

To provide a rigorous, falsifiable investigation, the research is decomposed into five specific Secondary Research Questions. The first four address the quantitative machine learning and econometric components, each paired with formal null ($H_0$) and alternative ($H_1$) hypotheses. The fifth addresses the socio-technical and regulatory policy dimension.

---

### SRQ 1: Feature Predictability & Alternative Data Signals
* **Research Question:**  
  *Which non-traditional behavioral, digital wallet, and transaction-based features (e.g., transaction regularity, airtime recharge frequency, utility payment consistency) provide statistically significant predictive signal for credit default risk among thin-file borrowers?*

* **Formal Hypotheses:**
  $$\begin{aligned}
  H_{0,1}: & \quad \text{Alternative behavioral and transactional features do not provide statistically significant predictive} \\
           & \quad \text{power for distinguishing default from non-default outcomes } (p \ge 0.05 \text{ or Information Value } IV < 0.02). \\
  H_{1,1}: & \quad \text{Specific non-traditional behavioral indicators (such as transaction regularity and recharge stability)} \\
           & \quad \text{yield statistically significant predictive separation for credit default } (p < 0.05 \text{ and } IV \ge 0.10).
  \end{aligned}$$

* **Evaluation Protocol & Verification Mechanism:**
  * **Information Value (IV) and Weight of Evidence (WoE):** Traditional credit scorecard benchmark metrics to assess univariate predictive power.
  * **Mutual Information & Permutation Feature Importance:** Non-parametric evaluation of non-linear association with the default label.
  * **Statistical Testing:** Wald test on logistic regression coefficients and Mann-Whitney U tests on feature distributions between defaulters and non-defaulters.

---

### SRQ 2: Algorithmic Comparative Performance & Discrimination
* **Research Question:**  
  *How do non-linear ensemble algorithms (Random Forest and XGBoost) compare against interpretable baseline models (Logistic Regression and Decision Trees) in terms of discriminatory power (ROC-AUC, PR-AUC), cost-sensitive error rates (FNR/FPR), and probability calibration (Brier Score)?*

* **Formal Hypotheses:**
  $$\begin{aligned}
  H_{0,2}: & \quad \text{Gradient boosted and bagging ensemble models (XGBoost, Random Forest) do not significantly} \\
           & \quad \text{outperform the baseline linear scorecard (Logistic Regression) or Decision Tree on ROC-AUC and PR-AUC} \\
           & \quad (\Delta\text{ROC-AUC} \le 0, \; p \ge 0.05). \\
  H_{1,2}: & \quad \text{XGBoost achieves statistically superior discrimination (ROC-AUC and PR-AUC) and a lower False} \\
           & \quad \text{Negative Rate (FNR) compared to Logistic Regression and Decision Trees } (\Delta\text{ROC-AUC} > 0, \; p < 0.05).
  \end{aligned}$$

* **Evaluation Protocol & Verification Mechanism:**
  * **Discrimination:** Paired **DeLong Test** to determine statistical significance of ROC-AUC differences on the independent holdout set.
  * **Imbalance Assessment:** Precision-Recall AUC (**PR-AUC**) to penalize false alarms in low-default regimes.
  * **Cost-Sensitive Risk:** **False Negative Rate ($FNR = \frac{FN}{TP+FN}$)**: In lending, false negatives (granting credit to an applicant who defaults) inflict direct capital losses.
  * **Probability Calibration:** **Brier Score** and calibration curves (reliability diagrams) to ensure that predicted output probabilities accurately reflect true default frequencies, which is mandatory for loan pricing.

---

### SRQ 3: Model Interpretability & Explainability (XAI)
* **Research Question:**  
  *Can post-hoc explainability techniques (SHAP and LIME) provide faithful, case-level and global risk attribution for non-linear ensemble models that meet the transparency and adverse-action disclosure standards required by financial regulators?*

* **Formal Hypotheses:**
  $$\begin{aligned}
  H_{0,3}: & \quad \text{Post-hoc explainability methods (TreeSHAP) do not generate consistent, rank-stable explanations} \\
           & \quad \text{of credit risk drivers across validation folds } (\text{Spearman's rank correlation } \rho < 0.80). \\
  H_{1,3}: & \quad \text{TreeSHAP generates mathematically consistent, globally stable feature attributions } (\rho \ge 0.80) \\
           & \quad \text{while providing granular, case-specific local adverse-action explanations for individual rejected applicants.}
  \end{aligned}$$

* **Evaluation Protocol & Verification Mechanism:**
  * **Global Explanation Stability:** Spearman's rank correlation of top-10 SHAP feature importance values across 5 cross-validation folds.
  * **Adverse Action Fidelity:** Generation of individual waterfall plots translating negative SHAP attributions into human-interpretable reason codes (e.g., "Airtime recharge variance too high over preceding 90 days").
  * **LIME vs. SHAP Cross-Validation:** Checking agreement between local linear approximations (LIME) and additive Shapley values for boundary loan decisions.

---

### SRQ 4: Algorithmic Fairness & Bias Auditing
* **Research Question:**  
  *Do machine learning credit risk models trained on alternative data introduce or amplify disparate impact across demographic sub-populations (e.g., gender, geographical location/region), and can fairness-constrained post-processing reduce disparate outcomes without catastrophic degradation of default prediction?*

* **Formal Hypotheses:**
  $$\begin{aligned}
  H_{0,4}: & \quad \text{The baseline unconstrained machine learning model satisfies demographic parity and equal opportunity} \\
           & \quad \text{without explicit fairness interventions } (\text{Disparate Impact Ratio } DIR \ge 0.80). \\
  H_{1,4}: & \quad \text{The baseline model exhibits disparate impact } (DIR < 0.80) \text{ against historically marginalized or rural} \\
           & \quad \text{sub-groups, which can be mitigated via threshold optimization while preserving predictive integrity.}
  \end{aligned}$$

* **Evaluation Protocol & Verification Mechanism:**
  * **Disparate Impact Ratio (DIR):** Selection rate of unprivileged group divided by selection rate of privileged group (assessing compliance with the standard $80\%$ four-fifths rule).
  * **Equal Opportunity Difference (EOD):** Difference in True Positive Rates (default identification recall) across demographic groups to prevent predatory inclusion.
  * **Pareto Frontier Analysis:** Quantifying the exact trade-off between ROC-AUC loss and fairness metric improvement under post-processing threshold adjustments.

---

### SRQ 5: Socio-Technical & Regulatory Policy Alignment
* **Research Question:**  
  *How can the ADCAI machine learning framework be operationalized to comply with the testing covenants, consumer disclosure rules, and risk mitigation requirements of the Bank of Namibia's Revised Fintech Innovation Regulatory Framework 2026 (Regulatory Sandbox) and support the objectives of the Namibia Financial Sector Transformation Strategy 2025–2035?*

* **Methodological Protocol:**
  * **Documentary Policy Analysis:** Rigorous statutory and regulatory benchmarking against:
    1. *Bank of Namibia Revised Fintech Innovation Regulatory Framework 2026* (Eligibility criteria, 6–18 month sandbox lifecycle, consumer safeguard protocols, exit pathways).
    2. *Bank of Namibia Financial Sector Transformation Strategy 2025–2035* (Pillar on Access to Finance and SME Financial Inclusion).
    3. *Namibia Financial Institutions Supervisory Authority (NAMFISA) Microlending Act 7 of 2018* (Interest rate caps, reckless lending prohibitions, consumer disclosures).
  * **Socio-Technical Governance Synthesis:** Developing a comprehensive risk-management matrix addressing data privacy, algorithmic redress, consent architecture, and model governance for Namibian micro-lenders and digital banks.

---

## 3. Mapping Matrix: Objectives, Questions, Hypotheses & Thesis Chapters

| Proposal Sub-Objective | Secondary Research Question | Hypothesis | Methodological Tools | Target Thesis Chapter |
| :--- | :--- | :--- | :--- | :--- |
| **Obj 1 & 2: Feature Signals & Behavioral Proxies** | **SRQ 1** | $H_{0,1} \text{ vs } H_{1,1}$ | Weight of Evidence (WoE), Information Value (IV), Permutation Importance | **Chapter 3 & Chapter 4** |
| **Obj 1 & 3: Algorithmic Benchmarking** | **SRQ 2** | $H_{0,2} \text{ vs } H_{1,2}$ | Logistic Regression, Decision Tree, Random Forest, XGBoost; DeLong test, Brier Score | **Chapter 3 & Chapter 4** |
| **Obj 4: Model Interpretability** | **SRQ 3** | $H_{0,3} \text{ vs } H_{1,3}$ | TreeSHAP, LIME, Summary & Dependence Plots, Adverse Action Reason Codes | **Chapter 4 & Chapter 5** |
| **Obj 4: Algorithmic Fairness** | **SRQ 4** | $H_{0,4} \text{ vs } H_{1,4}$ | Disparate Impact Ratio (DIR), Demographic Parity, Equal Opportunity, Fairlearn | **Chapter 4 & Chapter 5** |
| **Obj 4: Regulatory Operationalization** | **SRQ 5** | Policy Inquiry | BoN Fintech Sandbox 2026 Analysis, NFSTS 2025–2035 Benchmarking | **Chapter 2 & Chapter 5** |

---

## 4. Next Steps
Upon your review and approval of these formal research questions and hypotheses, we will advance directly to **STAGE 3: Conduct a literature and data-source investigation** to build the comprehensive Literature Matrix and evaluate candidate datasets.
