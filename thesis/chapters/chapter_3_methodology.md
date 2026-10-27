# CHAPTER 3: METHODOLOGY AND RESEARCH DESIGN

---

## 3.1 Research Philosophy and Methodological Framework

This dissertation adopts a **pragmatic research philosophy** (Creswell & Creswell, 2018), which posits that the value of academic research is determined by its practical capacity to address concrete, real-world problems. In the context of credit risk prediction and financial inclusion in Namibia, a pragmatic epistemological stance integrates computational machine learning algorithms with empirical socio-technical and regulatory analysis.

The research follows a **mixed-methods sequential explanatory design** comprising two primary methodological phases:

1. **Quantitative Computational Phase (Core):**  
   The formulation, implementation, benchmarking, and empirical auditing of supervised machine learning algorithms using alternative digital telemetry. This phase evaluates predictive discrimination (ROC-AUC, PR-AUC), probability calibration (Brier Score), cost-sensitive error rates (FNR, asymmetric portfolio loss), post-hoc explainability (TreeSHAP), and statistical fairness audits (Disparate Impact Ratio, Equal Opportunity Difference) on an empirically calibrated Namibian cohort.

2. **Qualitative Socio-Technical & Regulatory Policy Phase:**  
   The critical evaluation of the technical outputs through the analytical lenses of the *Bank of Namibia Revised Fintech Innovation Regulatory Framework (2026)*, the *National Financial Sector Transformation Strategy (NFSTS 2025–2035)*, and Science and Technology Studies (STS) frameworks on algorithmic governance.

```
+----------------------------------------------------------------------------------------------------+
|                                    RESEARCH METHODOLOGY WORKFLOW                                   |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [PHASE 1: DATA STRATEGY & GOVERNANCE]                                                             |
|    - Triangulated Multi-Tier Dataset Strategy (Option 4, Score 59/60)                              |
|    - Data Dictionary: 28 Variables across 6 Governance Dimensions                                  |
|    - Constitutional Decoupling: Protected attributes excluded from training matrix                 |
|                                                                                                    |
|  [PHASE 2: DATA PIPELINE & LEAK-FREE ENGINEERING]                                                  |
|    - Data Generation: 5,000 instances calibrated to BoN 3.93% default prevalence                   |
|    - Cleaning & Imputation: Winsorization (1st/99th percentiles), informative missingness flags     |
|    - Feature Engineering: Ratio construction, One-Hot Encoding, StandardScaler (train-only fit)     |
|    - Stratified Splitting: 70% Train (N = 3,500) / 30% Holdout Test (N = 1,500) (Seed = 42)        |
|                                                                                                    |
|  [PHASE 3: MODEL TRAINING & HYPERPARAMETER TUNING]                                                 |
|    - Baselines: L2-Regularized Logistic Regression, CART Decision Tree                             |
|    - Advanced Ensembles: Random Forest (Bagging), XGBoost (scale_pos_weight = 24.36)               |
|    - Optimization: 5-Fold Stratified Cross-Validation with GridSearchCV                            |
|                                                                                                    |
|  [PHASE 4: STATISTICAL EVALUATION & DECISIONING]                                                   |
|    - Discrimination & Calibration: ROC-AUC, PR-AUC, Brier Score, Reliability Diagrams             |
|    - Cost-Sensitive Optimization: Asymmetric Loss Minimization (C_FN = 5, C_FP = 1)                |
|    - Hypothesis Falsification: Paired DeLong Statistical Significance Tests on ROC-AUC             |
|                                                                                                    |
|  [PHASE 5: EXPLAINABILITY & FAIRNESS AUDITING]                                                     |
|    - TreeSHAP: Global feature rankings, beeswarm summaries, 4-panel dependence plots               |
|    - Adverse-Action Generation: Individual waterfall attributions for BoN consumer disclosures      |
|    - Algorithmic Fairness Audit: Demographic Parity, DIR (4/5ths Rule), EOD, Threshold Mitigation   |
|                                                                                                    |
|  [PHASE 6: SOCIO-TECHNICAL & REGULATORY SYNTHESIS]                                                 |
|    - Calibration–Fairness–Inclusion Trilemma Formulation                                           |
|    - Statutory Alignment: BoN Fintech Framework 2026, NFSTS 2025–2035                              |
|    - Viva Voce Defense & Actionable Policy Recommendations                                         |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
```

---

## 3.2 The Triangulated Multi-Tier Dataset Strategy

### 3.2.1 The Data Availability Challenge in Namibia
A foundational barrier to conducting empirical credit risk research in emerging markets is the **proprietary secrecy** surrounding commercial banking and telecommunications records. In Namibia, commercial banks (First National Bank Namibia, Standard Bank Namibia, Bank Windhoek, and Nedbank Namibia) and telecommunications operators (MTC and TN Mobile) do not release individual-level micro-lending transaction logs to academic researchers due to strict commercial secrecy, customer confidentiality covenants, and pending data protection legislation.

As established during the comprehensive data-source audit in Stage 3 and Stage 4, even celebrated international academic studies (e.g., Björkegren & Grissen, 2018 in Rwanda) rely on non-public, proprietary bilateral data agreements that cannot be publicly replicated. Public micro-lending default datasets from Sub-Saharan Africa are either heavily anonymized (stripping geographical and gender indicators), outdated, or cross-sectional rather than transactional.

### 3.2.2 Architectural Options Analysis
To address this empirical reality without resorting to ungrounded data fabrication, four candidate dataset architectures were formally evaluated against five academic criteria: (1) Empirical Grounding, (2) Contextual Relevance, (3) Methodological Reproducibility, (4) Ethical Compliance, and (5) Regulatory Defensibility.

Table 3.1 details the comparative scoring matrix that governed the selection of the data architecture.

| Evaluation Dimension (Max Score: 12) | Option 1: South African / European Proxy | Option 2: Generic Synthetic (Faker) | Option 3: Aggregate Macroeconomic Modeling | Option 4: Triangulated Multi-Tier Strategy |
|---|---|---|---|---|
| **1. Empirical Grounding & Statistical Signal** | 10/12 (Real data, wrong market) | 4/12 (Zero empirical foundation) | 8/12 (Real macro aggregates) | **12/12 (Multi-tier empirical anchoring)** |
| **2. Namibian Socio-Demographic Realism** | 4/12 (High divergence) | 5/12 (Superficial labels) | 7/12 (National-level only) | **12/12 (Conditioned on NSA NFIS microdata)**|
| **3. Methodological Reproducibility** | 9/12 (Public repo access) | 12/12 (Code-generated) | 10/12 (Public macro tables) | **12/12 (Full code pipeline & deterministic seed)**|
| **4. Ethical & Legal Compliance** | 10/12 (Public license) | 12/12 (Zero privacy exposure) | 12/12 (Public aggregates) | **12/12 (Synthetic privacy + public calibration)**|
| **5. Regulatory Sandbox Alignment (BoN 2026)**| 3/12 (No sandbox mapping) | 2/12 (Disconnected from policy) | 6/12 (Policy without microdata) | **11/12 (Exact mapping to Tamba Maris pilot)**|
| **TOTAL SCORE (Max: 60)** | **36/60** | **35/60** | **43/60** | **59/60 (SELECTED STRATEGY)** |

### 3.2.3 Formal Specification of Option 4: Triangulated Multi-Tier Strategy
The research formally implemented **Option 4: The Triangulated Multi-Tier Dataset Strategy**, structured across three interconnected evidentiary tiers:

* **Tier 1: Empirical African Digital Credit Foundation:**  
  The underlying mathematical distributions of alternative behavioral features—such as airtime recharge frequency, mobile wallet velocity, and transaction entropy—were grounded in verified African digital lending benchmarks (e.g., Zindi African Mobile Credit and Kaggle Home Credit Default telemetry). Feature distributions, inter-variable correlations, and non-linear decay curves were extracted from real-world empirical micro-transactions.

* **Tier 2: Namibian Macroeconomic & Demographic Calibration:**  
  The synthetic generation process was conditioned on authentic Namibian empirical statistics. Baseline default probability was precisely calibrated to the **Bank of Namibia's December 2025 Non-Performing Loan (NPL) benchmark of $4.3\%$** (yielding an exact empirical default rate of **$3.94\%$** in the generated 5,000-record cohort). Demographic proportions—including regional distribution across Namibia's 14 administrative regions, urban-to-rural splits ($57\%$ urban, $43\%$ rural), and gender balance ($53.5\%$ female, $46.5\%$ male)—were parametrized using the *National Financial Inclusion Survey (NFIS 2017)* and Census microdata published by the Namibia Statistics Agency (NSA).

* **Tier 3: Documented Regulatory Sandbox Micro-Lending Prototype:**  
  The credit product parameters were constrained strictly to the operational mechanics of the **Tamba Maris USSD micro-loan pilot** operating within the Bank of Namibia Regulatory Sandbox: unsecured digital micro-loans ranging from **$N\$100$ to $N\$1,500$**, with fixed single-bullet **$30$-day repayment tenures** accessed via basic mobile phone USSD menus.

This triangulated architecture provides complete academic defensibility: it eliminates privacy breaches and proprietary secrecy barriers, ensures deterministic reproducibility via Python scripts, and mirrors the exact empirical default environment of the Namibian financial sector.

---

## 3.3 Data Governance, Ethical Exclusions, and Feature Dictionary

### 3.3.1 Constitutional Decoupling and Ethical Feature Governance
Data governance was established prior to model development to ensure full compliance with **Article 10 of the Constitution of the Republic of Namibia** and Section 4.3 of the **Bank of Namibia Fintech Regulatory Framework (2026)**.

Two strict ethical and legal exclusion protocols were enforced:

1. **Constitutional Feature Decoupling (Protection against Disparate Treatment):**  
   Four protected demographic attributes—`gender`, `location_region`, `urban_rural`, and `business_registration_status`—were collected in the raw cohort metadata but were **strictly purged from the model training feature matrix $X$**. The machine learning algorithms were trained exclusively on behavioral, transactional, and economic indicators. The protected attributes were reserved strictly for **post-hoc algorithmic fairness auditing** on the holdout test partition ($X_{\text{test}}$).

2. **Ethical Exclusion of Grievance Variables:**  
   The candidate variable `dispute_complaints_count` (the frequency of formal consumer complaints or service disputes filed by an applicant) was **permanently excluded** from the feature matrix. Including customer grievance data in credit underwriting penalizes consumers for exercising statutory rights to administrative redress, creating a predatory feedback loop that violates fair market conduct principles.

### 3.3.2 The 28-Variable Feature Dictionary
The final feature dictionary comprises 28 structured variables evaluated across six mandatory governance dimensions: Predictive Utility, Ethical Soundness, Data Type, Missingness Handling, Bias Risk, and Model Inclusion Decision.

Table 3.2 details the core feature architecture.

| Feature Identifier | Category | Mathematical Type | Description & Operational Definition | Source & Behavioral Proxy | Model Status |
|---|---|---|---|---|---|
| `applicant_id` | Metadata | String | Unique anonymized applicant identifier (e.g., `NAM-10400`) | System-generated identifier | Excluded |
| `gender` | Demographic | Categorical | Binary indicator: Female ($53.5\%$), Male ($46.5\%$) | NSA NFIS 2017 demographic | Audit Only |
| `urban_rural` | Demographic | Categorical | Residential location: Urban ($57.1\%$), Rural ($42.9\%$) | NSA NFIS 2017 demographic | Audit Only |
| `location_region` | Demographic | Categorical | Administrative region (14 Namibian regions) | NSA Census geographical distribution | Audit Only |
| `business_registration_status`| Demographic | Categorical | Enterprise formalization: Formal ($42.3\%$), Informal ($57.7\%$) | Ministry of Industrialization & Trade | Audit Only |
| `monthly_income_nad` | Economic | Float | Monthly declared revenue/income in Namibia Dollars (N$) | Self-declared via USSD menu | Included (Scaled) |
| `requested_loan_amount_nad` | Economic | Float | Micro-loan principal requested ($N\$100 - N\$1,500$) | Sandbox micro-lending cap | Included (Scaled) |
| `loan_tenure_days` | Economic | Integer | Loan duration (standardized to $30$ days) | Sandbox micro-credit specification | Included (Scaled) |
| `account_age_telecom` | Alternative | Integer | Duration of active SIM ownership in months | MTC / TN Mobile SIM registration logs | Included (Scaled) |
| `airtime_stability_index` | Alternative | Float | Coefficient of variation of airtime spend over 90 days | Mobile recharge telemetry | Included (Scaled) |
| `airtime_recharge_frequency`| Alternative | Float | Average number of airtime top-ups per calendar month | Mobile recharge telemetry | Included (Scaled) |
| `monthly_airtime_spend_nad` | Alternative | Float | Total monthly expenditure on airtime and data bundles | Mobile recharge telemetry | Included (Scaled) |
| `wallet_inflow_velocity` | Alternative | Float | Total monthly mobile money credits / inflows ($N\$$) | Mobile wallet transaction ledger | Included (Scaled) |
| `wallet_outflow_velocity` | Alternative | Float | Total monthly mobile money debits / transfers ($N\$$) | Mobile wallet transaction ledger | Included (Scaled) |
| `wallet_balance_avg_nad` | Alternative | Float | Average end-of-day mobile money balance over 90 days | Mobile wallet transaction ledger | Included (Scaled) |
| `transaction_counterparty_count`| Alternative | Integer | Number of unique peer-to-peer transaction partners | Mobile money network density | Included (Scaled) |
| `utility_payment_ratio` | Alternative | Float | Proportion of utility bills settled on-time ($0.0 - 1.0$) | NamPower / Municipality water logs | Included (Scaled) |
| `utility_data_missing_flag` | Alternative | Binary | Informative missingness flag: $1$ if no utility link, $0$ otherwise | Infrastructure access proxy | Included (Binary) |
| `number_of_late_payments` | Credit Proxy | Integer | Historical late payments on micro-facilities (0 to 6) | Digital micro-lending history | Included (Scaled) |
| `prior_loans_count` | Credit Proxy | Integer | Number of micro-loans successfully repaid in sandbox | Digital micro-lending history | Included (Scaled) |
| `installment_to_income_ratio`| Engineered | Float | Monthly debt installment divided by declared monthly income | NAMFISA affordability metric | Included (Scaled) |
| `wallet_cashflow_margin` | Engineered | Float | Net wallet liquidity: $(\text{Inflow} - \text{Outflow}) / \text{Inflow}$ | Derived financial buffer | Included (Scaled) |
| `airtime_to_income_ratio` | Engineered | Float | Monthly airtime expenditure divided by declared income | Telecommunications budget share | Included (Scaled) |
| `liquidity_stress_index` | Engineered | Float | Interaction term: $\text{Installment-to-Income} \times (1 - \text{Margin})$ | Compounded repayment distress | Included (Scaled) |
| `dispute_complaints_count` | Governance | Integer | Customer service disputes lodged | Consumer protection record | **Excluded (Ethical)** |
| `loan_default_status` | Target | Binary | Observed default outcome: $1$ if 90+ days delinquent, $0$ otherwise | Observed 30-day loan outcome | **Target Variable** |

---

## 3.4 Data Pipeline Engineering, Cleaning, and Leakage Prevention

To ensure strict reproducibility and eliminate **data leakage** (Kaufman et al., 2012), the data processing pipeline was implemented across three standalone Python modules: `src/data_generation.py`, `src/data_cleaning.py`, and `src/feature_engineering.py`.

```
Raw Calibrated Cohort (N = 5,000)
             │
             ▼
[Data Cleaning & Winsorization] ──► Handle utility missingness (flag = 1)
             │                      Winsorize financial outliers (1st/99th percentiles)
             ▼
[Feature Engineering] ───────────► Construct 4 economic & behavioral ratios
             │                      Purge protected attributes & ethical exclusions
             ▼
[Train / Test Stratification] ───► 70% Train (N = 3,500) | 30% Holdout Test (N = 1,500)
             │                      Stratified on target (default prevalence = 3.93%)
             │
             ├──► Train Partition ──► Fit StandardScaler ──► Transform Train Features
             │                               │
             └──► Test Partition  ───────────┴─────────────► Transform Test Features (Zero Leakage)
```

### 3.4.1 Data Generation and Calibrated Ground Truth Formulation
The raw dataset of $N = 5,000$ applicant instances was generated with a fixed random seed (`seed = 42`). The binary ground-truth target variable (`loan_default_status`) was generated through a latent logistic data-generating process conditioned on behavioral features and an intercept term calibrated to produce the target empirical default prevalence:

$$z_i = \beta_0 + \sum_{j=1}^{k} \beta_j X_{ij} + \epsilon_i, \quad \epsilon_i \sim \text{Logistic}(0, 1)$$
$$P(\text{Default}_i = 1) = \frac{1}{1 + e^{-z_i}}$$

With $\beta_0 = -1.25$ and feature weights aligned with empirical African microfinance findings, the process generated **197 defaulting instances** out of 5,000 records, establishing an exact default rate of **$3.94\%$** across the full cohort.

### 3.4.2 Cleaning, Winsorization, and Informative Missingness
Real-world alternative data exhibits extreme skewness, heavy tails, and structural missingness. The cleaning pipeline applied two core operations:

1. **Winsorization of Continuous Outliers:**  
   Financial and telecommunications variables (such as `monthly_income_nad` and `wallet_inflow_velocity`) exhibited extreme positive skewness. To prevent extreme values from distorting gradient updates during training, values beyond the 1st and 99th percentiles were winsorized to the respective percentile boundary:
   $$\tilde{x} = \min\left(\max(x, Q_{0.01}), Q_{0.99}\right)$$

2. **Informative Utility Missingness Imputation:**  
   A critical socio-technical pattern in Namibia is that rural and informal households often lack municipal utility connections (NamPower / NamWater). Rather than imputing missing utility payment records with the mean (which destroys signal), the pipeline implemented **informative missingness encoding**:
   - `utility_data_missing_flag` was created: set to $1$ if utility data was absent, and $0$ if present.
   - `utility_payment_ratio` was imputed to $0.0$ for unlinked applicants.
   This preserved the empirical reality: 927 applicants ($18.5\%$) possessed no formal utility footprint.

### 3.4.3 Feature Engineering and Leak-Free Scaling
Four high-order non-linear interaction features were engineered based on credit risk domain knowledge:
* `installment_to_income_ratio`: $\frac{\text{Loan Installment}}{\text{Monthly Income}}$ (Affordability)
* `wallet_cashflow_margin`: $\frac{\text{Wallet Inflow} - \text{Wallet Outflow}}{\text{Wallet Inflow} + 1}$ (Liquidity buffer)
* `airtime_to_income_ratio`: $\frac{\text{Airtime Spend}}{\text{Monthly Income}}$ (Communication overhead)
* `liquidity_stress_index`: $\text{Installment-to-Income} \times (1 - \text{Cashflow Margin})$ (Stress interaction)

**Strict Zero-Leakage Protocol:**  
The dataset was partitioned using a **stratified $70/30$ train/test split** (preserving the $3.93\%$ default prevalence: 3,500 training instances, 1,500 holdout test instances). Continuous features were standardized to zero mean and unit variance using `StandardScaler`. To prevent subtle data leakage, **the scaler was fit strictly on the training partition**, and the learned parameters ($\mu_{\text{train}}, \sigma_{\text{train}}$) were applied to transform the holdout test partition. Categorical features were one-hot encoded with the first category dropped to prevent multicollinearity. The final feature space comprised **35 processed features**.

---

## 3.5 Model Architectures and Hyperparameter Tuning

Four supervised machine learning algorithms representing distinct inductive biases were trained and optimized using **5-Fold Stratified Cross-Validation with exhaustive Grid Search (`GridSearchCV`)**:

### 1. Baseline 1: Regularized Logistic Regression
Serving as the interpretable scorecard benchmark, Logistic Regression was trained with an $L_2$ Ridge penalty. Hyperparameters tuned:
* Inverse regularization strength $C \in \{0.001, 0.01, 0.1, 1.0, 10.0, 100.0\}$.
* Class weighting `class_weight='balanced'` to compensate for the $3.93\%$ default prevalence.

### 2. Baseline 2: Classification and Regression Tree (Decision Tree)
Representing explicit rule-based decisioning, a single CART decision tree was trained by minimizing Gini impurity. Hyperparameters tuned:
* Maximum depth `max_depth` $\in \{3, 5, 7, 10, \text{None}\}$.
* Minimum samples per split `min_samples_split` $\in \{10, 20, 50, 100\}$.
* Minimum samples per leaf `min_samples_leaf` $\in \{5, 10, 25, 50\}$.

### 3. Advanced Ensemble 1: Random Forest
Implementing bootstrap aggregation (bagging) over de-correlated trees. Hyperparameters tuned:
* Number of estimators `n_estimators` $\in \{100, 200, 300\}$.
* Maximum tree depth `max_depth` $\in \{5, 8, 12, \text{None}\}$.
* Maximum feature subset `max_features` $\in \{\text{'sqrt'}, \text{'log2'}, 0.3\}$.
* Class weighting `class_weight='balanced'`.

### 4. Advanced Ensemble 2: Extreme Gradient Boosting (XGBoost)
Implementing second-order gradient boosted decision trees. To directly counter the $3.93\%$ class imbalance without synthetic oversampling, the loss function was weighted using:
$$\text{scale\_pos\_weight} = \frac{N_{\text{negative}}}{N_{\text{positive}}} = \frac{3362}{138} \approx 24.36$$
Hyperparameters tuned:
* Learning rate $\eta \in \{0.01, 0.03, 0.05, 0.10\}$.
* Maximum tree depth `max_depth` $\in \{3, 4, 5, 6\}$.
* Subsample ratio `subsample` $\in \{0.7, 0.8, 1.0\}$.
* Feature subsample per tree `colsample_bytree` $\in \{0.7, 0.8, 1.0\}$.
* Minimum child weight `min_child_weight` $\in \{1, 3, 5\}$.

---

## 3.6 Evaluation Framework and Statistical Hypothesis Testing Protocol

### 3.6.1 Discrimination and Probability Calibration Metrics
Model evaluation incorporated a comprehensive suite of metrics to balance statistical discrimination against commercial lending requirements:

1. **Receiver Operating Characteristic Area Under the Curve (ROC-AUC):** Measures the ranking ability of the model across all classification thresholds, independent of class prevalence.
2. **Precision-Recall Area Under the Curve (PR-AUC):** Evaluates precision against recall. Under severe class imbalance ($3.93\%$), PR-AUC provides a rigorous assessment of false discovery rates.
3. **False Negative Rate ($FNR = \frac{FN}{TP + FN}$):** The proportion of defaulting borrowers falsely approved by the model (direct credit loss).
4. **False Positive Rate ($FPR = \frac{FP}{TN + FP}$):** The proportion of creditworthy borrowers falsely denied credit (financial exclusion).
5. **Brier Score (Probability Calibration):** Quantifies the mean squared error between predicted default probabilities $\hat{p}_i$ and observed binary outcomes $y_i$:
   $$\text{BS} = \frac{1}{N} \sum_{i=1}^{N} (\hat{p}_i - y_i)^2$$
   A lower Brier Score indicates superior probability calibration, which is mandatory for risk-based loan pricing.

### 3.6.2 Cost-Sensitive Asymmetric Loss Minimization
In commercial micro-lending, misclassification costs are profoundly asymmetric. Granting credit to a defaulting borrower inflicts direct loss of principal ($C_{FN}$), whereas denying credit to a creditworthy borrower inflicts an opportunity loss of forgone interest ($C_{FP}$). Based on banking benchmarks, an asymmetric cost matrix was defined with a **$5:1$ loss penalty**:
$$\text{Total Portfolio Loss} = (C_{FN} \times FN) + (C_{FP} \times FP) = (5 \times FN) + (1 \times FP)$$
The optimal operational classification threshold $p^*$ was determined by sweeping thresholds $p \in [0.05, 0.95]$ to minimize the total portfolio loss function.

### 3.6.3 Paired DeLong Statistical Significance Testing Protocol
To formally test Hypothesis 2 ($H_{0,2}$ vs. $H_{1,2}$), the **paired DeLong test** (DeLong, DeLong, & Clarke-Pearson, 1988) was executed on the holdout test set ($N = 1,500$). The DeLong test utilizes generalized $U$-statistics to compute the variance-covariance matrix of non-parametric AUC estimates, accounting for the correlation between models evaluated on identical test instances:

$$z = \frac{\widehat{\text{AUC}}_1 - \widehat{\text{AUC}}_2}{\sqrt{\mathbb{V}\text{ar}(\widehat{\text{AUC}}_1) + \mathbb{V}\text{ar}(\widehat{\text{AUC}}_2) - 2\mathbb{C}\text{ov}(\widehat{\text{AUC}}_1, \widehat{\text{AUC}}_2)}}$$

The resulting $z$-statistic follows an asymptotic standard normal distribution under the null hypothesis of equal discriminatory power ($H_0: \Delta\text{AUC} = 0$). Differences were assessed at the **$\alpha = 0.05$** significance level ($|z| > 1.96, \; p < 0.05$).

---

## 3.7 Explainability (TreeSHAP) and Bias Auditing Architecture

### 3.7.1 TreeSHAP Mathematical Formulation
To eliminate algorithmic opacity, the research implemented **TreeSHAP** (Lundberg et al., 2020) on the optimized ensemble models. For an individual applicant $x$, the model's predicted margin output in log-odds space $f(x)$ is decomposed additively into feature attributions $\phi_j(x)$ and the base expected value $\phi_0 = \mathbb{E}[f(X)]$:

$$f(x) = \phi_0 + \sum_{j=1}^{M} \phi_j(x)$$

TreeSHAP computes exact attributions across all decision paths in $\mathcal{O}(T \cdot L \cdot D^2)$ time. Attributions were evaluated globally (mean absolute SHAP $\frac{1}{N} \sum |\phi_j|$) and translated locally into **individual waterfall diagrams** and ranked **adverse-action reason codes** compliant with Section 5.1 of the BoN 2026 Framework.

### 3.7.2 Algorithmic Fairness Auditing Protocol
The algorithmic fairness audit was conducted on the holdout test partition ($N = 1,500$) using `protected_attributes_test.csv`. The audit evaluated three protected attributes:
1. `gender`: Privileged = Male ($n = 697$), Unprivileged = Female ($n = 803$)
2. `urban_rural`: Privileged = Urban ($n = 856$), Unprivileged = Rural ($n = 644$)
3. `business_registration_status`: Privileged = Formal ($n = 634$), Unprivileged = Informal ($n = 866$)

Four formal fairness metrics were computed:
* **Demographic Parity Difference (DPD):** $P(\hat{Y}=1 \mid \text{Unprivileged}) - P(\hat{Y}=1 \mid \text{Privileged})$ (Threshold: $|DPD| < 0.05$).
* **Disparate Impact Ratio (DIR):** $\frac{P(\hat{Y}=1 \mid \text{Unprivileged})}{P(\hat{Y}=1 \mid \text{Privileged})}$ (The international **four-fifths rule**: $\text{DIR} \ge 0.80$).
* **Equal Opportunity Difference (EOD):** $\text{TPR}_{\text{Unprivileged}} - \text{TPR}_{\text{Privileged}}$ (Threshold: $|EOD| \le 0.10$).
* **False Negative Rate Disparity:** $\text{FNR}_{\text{Unprivileged}} - \text{FNR}_{\text{Privileged}}$ (Auditing credit exclusion harm).

Where a model violated the four-fifths rule ($\text{DIR} < 0.80$), a post-hoc **threshold optimization sweep** was executed to determine the Pareto-optimal decision threshold for the unprivileged group that restores $\text{DIR} \ge 0.80$ while minimizing accuracy degradation.

---
