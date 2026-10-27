# Credit-Risk Data Dictionary & Variable Governance Framework

**Candidate:** Percyviarance Minsozi Simasiku (201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** Alternative Data, Mobile Money, Utility Transactions, SME Features, Demographic Ethics, and Target Variable Definition  

---

## 1. Target Variable Formulation

Under the Basel Committee on Banking Supervision (BCBS) prudential standards and the Bank of Namibia's Regulatory Sandbox directives, credit risk cannot be formulated merely on subjective or arbitrary labels.

* **Target Name:** `loan_default_flag` (Ground-Truth Binary Indicator)
* **Mathematical Definition:**
  $$Y_i = \begin{cases} 1, & \text{if borrower } i \text{ defaults (delinquent } \ge 90 \text{ days past due or failed settlement/chargeback)} \\ 0, & \text{if borrower } i \text{ successfully repays the loan on or before due date} \end{cases}$$
* **Model Output Target:** $\hat{p}_i = P(Y_i = 1 \mid \mathbf{X}_i)$ (Calibrated Continuous Probability of Default).
* **Decision Threshold ($p_{\text{cutoff}}$):** Calibrated against the empirical baseline individual NPL rate in Namibia ($4.3\%$ as of Dec 2025; $5.9\%$ in 2023) and asymmetric misclassification costs ($C_{\text{FN}} \gg C_{\text{FP}}$):
  $$\hat{Y}_i = \begin{cases} 1 (\text{Reject / High Risk}), & \text{if } \hat{p}_i \ge p_{\text{cutoff}} \\ 0 (\text{Approve / Low-Medium Risk}), & \text{if } \hat{p}_i < p_{\text{cutoff}} \end{cases}$$

---

## 2. Comprehensive Data Dictionary (28 Variables Across 6 Categories)

Below is the exhaustive evaluation of all candidate variables across the six mandatory criteria:
1. **Predictive Rationale:** Why it predicts credit risk.
2. **Legal & Ethical Appropriateness:** Compliance with the Namibian Constitution (Art. 10 equality), NAMFISA Microlending Act 2018, and BoN Consumer Safeguards.
3. **Data Type:** Continuous, Integer, Categorical, Binary.
4. **Expected Missingness:** Frequency of missing values and required imputation approach.
5. **Possible Bias & Proxy Risks:** Risk of encoding discrimination against protected or vulnerable sub-populations.
6. **Final Model Inclusion Decision:** `[INCLUDED]` as direct predictive feature, `[RETAINED_FAIRNESS_ONLY]` strictly for bias auditing and not exposed to the training model, or `[EXCLUDED]` entirely due to legal, ethical, or noise concerns.

---

### Category A: Alternative Digital & Mobile Telecommunications Features

#### 1. `airtime_recharge_frequency` (Recharges per Month)
* **Predictive Rationale:** High and consistent recharge frequency reflects stable liquidity, daily disposable cash flow, and routine behavioral discipline (Björkegren & Grissen, 2020).
* **Legal/Ethical Appropriateness:** Fully appropriate; non-invasive behavioral summary derived from standard telco billing logs with user consent.
* **Data Type:** Continuous (Float).
* **Expected Missingness:** Low (<1.0%); median imputation.
* **Possible Bias:** May slightly penalize rural subsistence farmers who purchase large single vouchers seasonally; mitigate through seasonal normalization.
* **Model Decision:** `[INCLUDED]` (Primary alternative signal).

#### 2. `airtime_recharge_volatility` (Coefficient of Variation of Recharge Amounts)
* **Predictive Rationale:** Erratic fluctuations in voucher purchase amounts indicate cash flow instability and income shocks, correlated with default likelihood.
* **Legal/Ethical Appropriateness:** Fully appropriate; objective statistical variance metric.
* **Data Type:** Continuous (Float).
* **Expected Missingness:** Low (<2.0%); imputed with median.
* **Possible Bias:** Minimal direct socio-economic bias.
* **Model Decision:** `[INCLUDED]`.

#### 3. `mobile_wallet_txn_regularity` (Entropy / Regularity of Wallet Outflows)
* **Predictive Rationale:** Regular, predictable weekly transaction outflow schedules serve as a direct proxy for recurring business activity or personal budgeting discipline.
* **Legal/Ethical Appropriateness:** Fully appropriate under BoN Fintech Sandbox consent guidelines.
* **Data Type:** Continuous (Normalized index $0.0 - 1.0$).
* **Expected Missingness:** Low (<1.0%); zero-fill or median.
* **Possible Bias:** Dependent on mobile wallet agent network coverage; rural users may have fewer transactions.
* **Model Decision:** `[INCLUDED]`.

#### 4. `p2p_transfer_in_out_ratio` (Inbound vs Outbound P2P Transfer Ratio)
* **Predictive Rationale:** Net receivers of funds indicate informal remittances or merchant revenue; high outbound draining without replenishment signals insolvency.
* **Legal/Ethical Appropriateness:** Highly appropriate financial velocity measure.
* **Data Type:** Continuous (Float).
* **Expected Missingness:** Low (<3.0%); bounded at $[0, 10]$.
* **Possible Bias:** Remittance-dependent households might show high ratios; valid economic signal.
* **Model Decision:** `[INCLUDED]`.

#### 5. `utility_bill_payment_consistency` (Percentage of Utility Bills Paid on Time)
* **Predictive Rationale:** Routine payment of municipal electricity (e.g., NamPower / City of Windhoek) or water bills demonstrates debt-servicing willingness and forward financial planning.
* **Legal/Ethical Appropriateness:** Standard credit bureau substitute; highly defensible.
* **Data Type:** Continuous (Percentage $0.0 - 1.0$).
* **Expected Missingness:** Moderate (~15% due to prepaid electricity / communal water); flag missingness explicitly with indicator variable.
* **Possible Bias:** Rural or informal settlement residents lacking formal utility connections would suffer missingness. Must not automatically assign high default risk to missing utility records.
* **Model Decision:** `[INCLUDED]` (with missingness indicator).

#### 6. `account_age_telecom` (Months Since SIM / Wallet Registration)
* **Predictive Rationale:** Account longevity indicates socio-economic stability and lower identity churn; fly-by-night or fraudulent borrowers frequently use newly registered SIMs.
* **Legal/Ethical Appropriateness:** Legally sound under CRAN SIM-registration regulations in Namibia.
* **Data Type:** Integer (Months).
* **Expected Missingness:** Zero (<0.1%).
* **Possible Bias:** Newer mobile subscribers (young adults or recently relocated individuals) may receive slightly lower baseline tenure points.
* **Model Decision:** `[INCLUDED]`.

---

### Category B: Micro-Enterprise & Informal Business Characteristics

#### 7. `business_type` (Retail, Service, Agriculture, Artisan, Street Merchant)
* **Predictive Rationale:** Cash-flow cyclicity varies drastically between street vending (daily cash) and agriculture (seasonal crop/livestock sales).
* **Legal/Ethical Appropriateness:** Standard business underwriting factor.
* **Data Type:** Categorical (Nominal).
* **Expected Missingness:** Low (<2.0%); imputed as "General/Other".
* **Possible Bias:** Risk of redlining specific informal sectors; ensure balanced weight through cross-validation.
* **Model Decision:** `[INCLUDED]`.

#### 8. `years_in_operation` (Business Tenure)
* **Predictive Rationale:** Empirical SME literature (Beck & Demirguc-Kunt, 2006) shows business survival rates jump substantially after 2–3 years; older informal businesses have stabilized client bases.
* **Legal/Ethical Appropriateness:** Fully appropriate.
* **Data Type:** Continuous (Years).
* **Expected Missingness:** Low (<3.0%); median imputation.
* **Possible Bias:** Inherently disadvantages younger entrepreneurs; must be balanced with transaction velocity.
* **Model Decision:** `[INCLUDED]`.

#### 9. `monthly_revenue_estimated` (Estimated Monthly Turnover in N$)
* **Predictive Rationale:** Determines debt capacity and debt-service coverage ratio (DSCR).
* **Legal/Ethical Appropriateness:** Mandatory under NAMFISA Microlending Act 2018 affordability assessment regulations.
* **Data Type:** Continuous (Monetary N$).
* **Expected Missingness:** Moderate (~10%–15% in informal self-reports); robust median by business type.
* **Possible Bias:** Self-reporting bias; verify against digital wallet inflows.
* **Model Decision:** `[INCLUDED]`.

#### 10. `monthly_operating_expenses` (Estimated Operating Costs in N$)
* **Predictive Rationale:** High overhead relative to turnover restricts residual free cash flow available to service loans.
* **Legal/Ethical Appropriateness:** Mandatory for reckless lending prevention.
* **Data Type:** Continuous (Monetary N$).
* **Expected Missingness:** Moderate (~12%); imputed using sectoral expense ratios.
* **Possible Bias:** Informal merchants often blend domestic and enterprise expenses.
* **Model Decision:** `[INCLUDED]`.

#### 11. `net_disposable_cashflow` (`monthly_revenue` - `monthly_expenses`)
* **Predictive Rationale:** Primary determinant of repayment ability; negative or razor-thin cash flow guarantees eventual default upon minor external shock.
* **Legal/Ethical Appropriateness:** Fully compliant and economically essential.
* **Data Type:** Continuous (Monetary N$).
* **Expected Missingness:** Calculated feature (missing if revenue or expense missing).
* **Possible Bias:** Reflects true economic affordability.
* **Model Decision:** `[INCLUDED]`.

#### 12. `business_registration_status` (Formal Registered vs. Informal Unregistered)
* **Predictive Rationale:** Formal businesses have greater legal recourse and stability, but informal businesses constitute 57.7% of Namibian employment.
* **Legal/Ethical Appropriateness:** Highly sensitive in financial inclusion.
* **Data Type:** Binary (`0` = Informal, `1` = Formal).
* **Expected Missingness:** Zero.
* **Possible Bias:** **High structural bias**. Penalizing informal businesses solely for being unregistered would defeat the entire purpose of the financial inclusion mandate in Namibia.
* **Model Decision:** `[EXCLUDED_FROM_MODEL / RETAINED_FAIRNESS_ONLY]` (Used to audit whether the model penalizes informal enterprises unfairly; not used as a negative feature in scoring).

#### 13. `financial_record_availability` (None, Paper Ledger, Mobile App, Bank Statements)
* **Predictive Rationale:** Maintaining some form of record (even a physical notebook) correlates with managerial competence and lower default risk.
* **Legal/Ethical Appropriateness:** Legally sound and constructive.
* **Data Type:** Categorical (Ordinal: 0 = None, 1 = Paper, 2 = Digital).
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Correlated with basic literacy and education.
* **Model Decision:** `[INCLUDED]`.

#### 14. `number_of_employees` (Firm Headcount)
* **Predictive Rationale:** Micro-enterprises with 1–4 employees show greater enterprise stability than solo survivalist traders.
* **Legal/Ethical Appropriateness:** Standard underwriting variable.
* **Data Type:** Integer.
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** Solo women street traders dominate informal retail; could penalize single-person operations.
* **Model Decision:** `[INCLUDED]`.

---

### Category C: Loan Facility & Credit Terms Features

#### 15. `loan_amount_requested` (Principal in N$)
* **Predictive Rationale:** Larger loan amounts increase debt burden and monthly installment pressure, elevating default risk if mismatched with income.
* **Legal/Ethical Appropriateness:** Universal credit underwriting feature.
* **Data Type:** Continuous (Monetary N$: typical range N\$100 to N\$5,000 for digital microlending).
* **Expected Missingness:** Zero (Mandatory input at application).
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 16. `loan_tenor_months` (Duration in Months)
* **Predictive Rationale:** Longer tenors extend default exposure over time; digital loans typically run 1 to 6 months.
* **Legal/Ethical Appropriateness:** Standard facility term.
* **Data Type:** Integer (e.g., 1, 3, 6, 12 months).
* **Expected Missingness:** Zero.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 17. `loan_purpose` (Working Capital, Equipment, Personal Emergency, Inventory)
* **Predictive Rationale:** Productive loans (inventory, equipment) generate cash returns to service debt; consumption loans (emergencies) rely on existing fixed income.
* **Legal/Ethical Appropriateness:** Standard KYC and credit appraisal field.
* **Data Type:** Categorical.
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Emergency personal loans are often required by lower-income households.
* **Model Decision:** `[INCLUDED]`.

#### 18. `installment_to_income_ratio` (Installment / Net Disposable Cash Flow)
* **Predictive Rationale:** The classic Debt-Service Ratio; ratios exceeding 30%–40% trigger sharp non-linear increases in default probability.
* **Legal/Ethical Appropriateness:** Legally mandatory under NAMFISA Microlending Act 2018 affordability caps.
* **Data Type:** Continuous (Ratio).
* **Expected Missingness:** Derived feature; bounded.
* **Possible Bias:** None; objective economic capacity metric.
* **Model Decision:** `[INCLUDED]`.

---

### Category D: Historical Borrowing & Savings Discipline

#### 19. `number_of_previous_loans` (Count of Past Borrowings)
* **Predictive Rationale:** Established borrowing history provides track record; zero previous loans indicates thin-file status.
* **Legal/Ethical Appropriateness:** Fully appropriate.
* **Data Type:** Integer.
* **Expected Missingness:** Zero.
* **Possible Bias:** Penalizes first-time borrowers unless offset by alternative digital signals.
* **Model Decision:** `[INCLUDED]`.

#### 20. `number_of_late_payments` (Past 30-Day Delinquency Count)
* **Predictive Rationale:** Past repayment behavior is empirically the single strongest predictor of future credit performance.
* **Legal/Ethical Appropriateness:** Core credit underwriting criterion.
* **Data Type:** Integer.
* **Expected Missingness:** Zero (defaults to 0 for thin-file).
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 21. `historical_default_count` (Number of Written-Off Facilities)
* **Predictive Rationale:** Past un-remedied defaults demonstrate severe credit risk.
* **Legal/Ethical Appropriateness:** Universally recognized credit metric.
* **Data Type:** Integer.
* **Expected Missingness:** Zero.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 22. `savings_deposit_frequency` (Monthly Micro-Savings Deposits)
* **Predictive Rationale:** Active participation in formal bank savings or informal savings groups (*stokvels* / rotating funds) demonstrates financial cushion and deferred consumption discipline.
* **Legal/Ethical Appropriateness:** Highly positive financial inclusion signal.
* **Data Type:** Integer (Deposits/month).
* **Expected Missingness:** Moderate (~10%); zero-fill.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

---

### Category E: Behavioral & Customer Interaction Data

#### 23. `digital_payment_adoption_ratio` (Digital Payments / Total Transactions)
* **Predictive Rationale:** Borrowers who actively use digital rails for payments generate richer data and exhibit higher technological fluency, correlated with modern business resilience.
* **Legal/Ethical Appropriateness:** Legally sound under digital economy policies.
* **Data Type:** Continuous (Ratio $0.0 - 1.0$).
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Skews towards urban centers with high merchant POS/QR adoption.
* **Model Decision:** `[INCLUDED]`.

#### 24. `dispute_complaints_count` (Billing or Service Inquiries Filed)
* **Predictive Rationale:** Frequent disputes may indicate dissatisfaction, service interruption, or contested fraudulent transactions.
* **Legal/Ethical Appropriateness:** Caution required; consumers must not be penalized for asserting legitimate consumer protection rights.
* **Data Type:** Integer.
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** **Ethical Risk**. Penalizing consumers for filing complaints violates Bank of Namibia consumer protection guidelines.
* **Model Decision:** `[EXCLUDED]` (Excluded on ethical grounds to protect consumer recourse rights).

---

### Category F: Protected Demographic Attributes & Fairness Auditing

#### 25. `applicant_age` (Age in Years)
* **Predictive Rationale:** Correlates with career stability, financial maturity, and lifecycle consumption.
* **Legal/Ethical Appropriateness:** Permissible for age-of-majority validation; restricted against ageist discrimination.
* **Data Type:** Integer (Years, $18 - 75$).
* **Expected Missingness:** Zero.
* **Possible Bias:** Younger borrowers have shorter histories; elderly borrowers face fixed income constraints.
* **Model Decision:** `[INCLUDED_WITH_FAIRNESS_CHECKS]` (Included for non-linear lifecycle modeling; audited across age brackets: 18–25, 26–45, 46+).

#### 26. `gender` (Female / Male)
* **Predictive Rationale:** Empirical literature (Suri & Jack, 2016) shows female informal entrepreneurs in Africa often have lower default rates.
* **Legal/Ethical Appropriateness:** **Strictly Prohibited under Article 10 of the Namibian Constitution (Equality and Freedom from Discrimination)** as a direct basis for denying credit.
* **Data Type:** Binary (`0` = Male, `1` = Female).
* **Expected Missingness:** Zero.
* **Possible Bias:** Direct discrimination risk.
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Strictly excluded from model input features $\mathbf{X}$; retained strictly in validation set to compute Disparate Impact Ratio and Equal Opportunity Difference).

#### 27. `location_region` (Namibian Administrative Regions: Khomas, Erongo, Ohangwena, Omusati, etc.)
* **Predictive Rationale:** Regional macroeconomic activity and drought susceptibility influence repayment.
* **Legal/Ethical Appropriateness:** High risk of geographic redlining.
* **Data Type:** Categorical (14 Regions).
* **Expected Missingness:** Zero.
* **Possible Bias:** High risk of acting as a proxy for ethnic origin or rural marginalization (violating Namibian Constitution Art. 10).
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Excluded from direct scoring; aggregated into `urban_rural` macro indicator only for fairness audits).

#### 28. `urban_rural` (Urban Center vs. Rural / Informal Settlement)
* **Predictive Rationale:** Rural communities face higher infrastructural and liquidity constraints (NSA reports 27.1% rural exclusion vs 17.5% urban).
* **Legal/Ethical Appropriateness:** Sensitive attribute.
* **Data Type:** Binary (`0` = Rural/Informal, `1` = Urban).
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** Using urban/rural as a direct rejection factor would entrench regional underdevelopment and violate the Financial Sector Transformation Strategy 2025–2035.
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Retained strictly as a protected attribute for group fairness auditing).

---

## 3. Variable Governance Summary Table

| Category | Total Proposed | Included in Model Features ($\mathbf{X}$) | Retained for Fairness Audit Only | Excluded Entirely |
| :--- | :---: | :---: | :---: | :---: |
| **Alternative & Telco Features** | 6 | 6 | 0 | 0 |
| **Business / Micro-Enterprise** | 8 | 7 | 1 (`business_registration_status`) | 0 |
| **Loan Terms & Debt Service** | 4 | 4 | 0 | 0 |
| **Repayment & Savings History**| 4 | 4 | 0 | 0 |
| **Behavioral & Complaints** | 2 | 1 | 0 | 1 (`dispute_complaints_count`) |
| **Protected Demographics** | 4 | 1 (`applicant_age`) | 3 (`gender`, `location_region`, `urban_rural`) | 0 |
| **Total Variables** | **28** | **23 Features in $\mathbf{X}$** | **4 Protected Attributes** | **1 Excluded Variable** |
