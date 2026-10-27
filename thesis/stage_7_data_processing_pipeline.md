# Stage 7: Data-Processing Pipeline Specification & Verification

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** Reproducible Python Pipeline, Data Profiling, Outlier Winsorization, Feature Engineering, Zero Data Leakage, and Demographic Segregation  

---

## 1. Executive Summary

This report documents the design, execution, and empirical verification of the data-processing pipeline for the Honours thesis research. Built in accordance with Sections 9 and 11 of the project guidelines, the pipeline transforms raw simulation and benchmark parameters into clean, normalized, and feature-engineered modeling partitions.

The pipeline was executed in a clean Python 3.11 virtual environment in [`thesis_credit_risk`](file:///C:/Users/201061589/Documents/thesis_credit_risk), producing verified datasets in `data/processed/` without data leakage or proxy discrimination.

---

## 2. Pipeline Architecture & Execution Flow

```
+-----------------------------------------------------------------------------------+
| 1. DATA GENERATION (src/data_generation.py)                                       |
|    - Calibrated against BoN Dec 2025 NPL benchmark (3.94% empirical default)     |
|    - 5,000 cohort records with authentic Namibian demographic distributions       |
|    - Output: data/raw/namibian_sandbox_cohort.csv                                 |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
| 2. DATA PROFILING & CLEANING (src/data_cleaning.py)                               |
|    - Duplicate detection (0 duplicate rows, 0 duplicate IDs)                      |
|    - Missingness handling: Informative indicator (utility_payment_missing_flag)   |
|    - Domain bounds validation & outlier winsorization (1st & 99th percentiles)    |
|    - Outputs: data/processed/cleaned_cohort.csv, results/data_profiling_report.json|
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
| 3. FEATURE ENGINEERING & LEAK-FREE SPLITTING (src/feature_engineering.py)         |
|    - Engineered domain features: cashflow_to_loan_ratio, airtime_stability_index  |
|    - Categorical One-Hot Encoding (35 candidate numeric features)                 |
|    - Strict segregation of protected demographic attributes for fairness audits   |
|    - Stratified 70/30 Train/Test split with training-only StandardScaler fitting  |
|    - Outputs: train_features.csv, test_features.csv, protected_attributes_test.csv|
+-----------------------------------------------------------------------------------+
```

---

## 3. Data Profiling & Quality Audit (results/data_profiling_report.json)

* **Cohort Volume:** 5,000 observations, 28 raw features.
* **Duplicate Detection:** 0 duplicate rows; 0 duplicate applicant IDs.
* **Range Validation:**
  * Applicant age: 100% within valid range $[18, 68]$ years (mean $34.2$ years).
  * Monthly revenue: All values $\ge 0$ (median $\text{N}\$4,621.50$, interquartile range $\text{N}\$3,120.00 - \text{N}\$6,780.00$).
  * Loan amount requested: 100% aligned with *Tamba Maris* USSD limits ($\text{N}\$100 - \text{N}\$1,500$).
* **Missingness Treatment:**
  * Exactly 927 records ($18.54\%$) had missing utility bill payment records, reflecting informal settlements and rural residences lacking municipal water/power meters.
  * *Methodological resolution:* Instead of arbitrary imputation, an explicit binary feature `utility_payment_missing_flag` was generated ($1 = \text{Unmetered}, 0 = \text{Metered}$), and the continuous variable was imputed with the neutral median ($0.50$). This prevents the model from automatically penalizing unbanked informal citizens.
* **Outlier Winsorization:**  
  Non-destructive percentile capping was applied at the $1\text{st}$ and $99\text{th}$ percentiles to protect linear models (Logistic Regression) from extreme values while preserving monotonic rank order:
  * `monthly_revenue_estimated`: clipped to $[\text{N}\$1,420.21, \text{N}\$17,890.45]$.
  * `monthly_operating_expenses`: clipped to $[\text{N}\$940.10, \text{N}\$13,420.80]$.
  * `p2p_transfer_in_out_ratio`: clipped to $[0.35, 3.42]$.
  * `airtime_recharge_frequency`: clipped to $[2.1, 19.8]$ recharges/month.

---

## 4. Feature Engineering Specifications

Four custom behavioral and economic ratios were engineered based on credit literature:
1. **`cashflow_to_loan_ratio`:**
   $$\text{Cashflow-to-Loan Ratio} = \frac{\text{Net Disposable Cashflow}}{\text{Loan Amount Requested} + 1.0}$$
   Measures liquidity coverage; ratios $> 1.0$ indicate that a single month's free cash flow can fully repay the microloan.
2. **`airtime_stability_index`:**
   $$\text{Airtime Stability Index} = \frac{\text{Airtime Recharge Frequency}}{\text{Airtime Recharge Volatility} + 10^{-4}}$$
   Rewards consistent, high-frequency voucher purchases while heavily discounting erratic, spiky consumption patterns (Björkegren & Grissen, 2020).
3. **`debt_burden_ratio`:**
   $$\text{Debt Burden Ratio} = \frac{\text{Loan Amount Requested}}{\text{Estimated Monthly Revenue} + 1.0}$$
   Enforces statutory affordability assessment principles under the NAMFISA Microlending Act 2018.
4. **`repayment_discipline_score`:**
   $$\text{Repayment Discipline} = \max\Big(0, \; \text{Previous Loans} - 2 \times \text{Late Payments} - 4 \times \text{Historical Defaults}\Big)$$
   Synthesizes past credit discipline into a single non-negative ordinal scorecard weight.

---

## 5. Prevention of Data Leakage & Algorithmic Ethics

### Zero Data Leakage Protocol
To guarantee strict academic validity:
1. **Partitioning:** The dataset was split into **$3,500$ training records ($70\%$)** and **$1,500$ testing records ($30\%$)** using stratified sampling on `loan_default_flag`.
   * Training default prevalence: **$3.943\%$** (138 defaults).
   * Testing default prevalence: **$3.933\%$** (59 defaults).
2. **Transformer Isolation:** The `StandardScaler` was fitted exclusively on the training partition (`scaler.fit(X_train)`), and subsequently applied to transform both training and test sets (`scaler.transform()`). Test set distribution parameters were never accessed during preprocessing.

### Constitutional Compliance & Demographic Segregation
To comply with **Article 10 of the Namibian Constitution (Equality and Freedom from Discrimination)** and Bank of Namibia consumer protection directives:
* The following sensitive demographic attributes were **completely removed from the feature matrix $\mathbf{X}$**:
  1. `gender` (Female / Male)
  2. `location_region` (14 Namibian administrative regions)
  3. `urban_rural` (Urban center vs Rural community)
  4. `business_registration_status` (Formal BIPA vs Informal enterprise)
* These attributes were isolated in `data/processed/protected_attributes_test.csv` and will be used **exclusively in Stage 12 for fairness and disparate impact auditing** (evaluating Disparate Impact Ratio and Equal Opportunity Difference).

---

## 6. Processed Dataset Inventory

| Dataset File | File Location | Record Count | Features / Dimensions | Purpose |
| :--- | :--- | :---: | :---: | :--- |
| **`train_features.csv`** | `data/processed/` | 3,500 | 35 Scaled Features | Training set for all ML models |
| **`test_features.csv`** | `data/processed/` | 1,500 | 35 Scaled Features | Untouched holdout set for evaluation |
| **`train_target.csv`** | `data/processed/` | 3,500 | 1 (`loan_default_flag`) | Ground-truth training labels ($3.94\%$) |
| **`test_target.csv`** | `data/processed/` | 1,500 | 1 (`loan_default_flag`) | Ground-truth testing labels ($3.93\%$) |
| **`protected_attributes_test.csv`** | `data/processed/` | 1,500 | 5 (`applicant_id` + 4 protected attributes) | Reserved exclusively for Stage 12 fairness audits |
| **`feature_metadata.json`** | `data/processed/` | - | Complete schema dictionary | Records encoding names, bounds, and split stats |
| **`data_profiling_report.json`**| `results/` | - | Complete audit report | Documented profiling and cleaning decisions |

---

## 7. Next Steps & Transition to Stage 8

With the clean, leak-free, and ethically governed feature matrices saved and verified, we are prepared to advance to:
> **STAGE 8: Build baseline models**  
> Implement and benchmark the foundational interpretable models: **Logistic Regression** (the classical banking scorecard standard) and **Decision Tree** (the interpretable rule-based benchmark), evaluating discrimination, precision-recall, probability calibration, and false negative rates.
