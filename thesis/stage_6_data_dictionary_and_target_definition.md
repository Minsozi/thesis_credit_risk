# Stage 6: Data Dictionary & Target Variable Formulation

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** 28-Variable Credit Risk Dictionary, Algorithmic Ethics, and Mathematical Formulation of Credit Risk  

---

## 1. Target Variable Formulation (Prompt Section 8)

The prompt template explicitly mandates investigating three possible formulations of credit risk:
1. **Default / No Default (Binary)**
2. **High Risk / Low Risk (Discretized Classes)**
3. **Probability of Default (Continuous Probability)**

### Comparative Academic Evaluation of Target Formulations

| Formulation | Mathematical Nature | Practical & Regulatory Suitability | Academic Assessment |
| :--- | :--- | :--- | :--- |
| **High Risk / Low Risk** | Coarse binary or ordinal discretization based on arbitrary score cutoffs. | Poor suitability in banking. Obscures true underlying default risk and makes risk-based loan pricing or loss provisioning impossible. | **Rejected:** Arbitrary risk binning creates artificial boundary effects and cannot be calibrated against central bank NPL rates. |
| **Default / No Default (Only)** | Pure binary classification label ($Y \in \{0, 1\}$) evaluated at a fixed 0.5 threshold. | Standard in introductory ML, but dangerous in real lending. Treating credit prediction as a hard $0/1$ decision ignores the confidence of the prediction and misclassification cost asymmetry. | **Insufficient on its own:** Ground-truth labels must be binary, but model outputs cannot be restricted to hard uncalibrated binary classes. |
| **Ground-Truth Binary Default with Calibrated Probability of Default ($\mathbf{PD}$)** | Supervised binary label ($Y \in \{0, 1\}$) paired with calibrated continuous risk score ($\hat{p} = P(Y=1 \mid \mathbf{X}) \in [0, 1]$). | **Gold Standard** in institutional banking (Basel II/III/IV Internal Ratings-Based approaches) and Bank of Namibia prudential reporting. Allows risk-based loan pricing, dynamic cutoff tuning, and calculation of Expected Loss ($EL = PD \times LGD \times EAD$). | **Adopted as Primary Formulation**: Scientifically rigorous, mathematically sound, and regulatory-compliant. |

### The Chosen Formulation
The research adopts **Ground-Truth Binary Default** as the training target, with **Calibrated Continuous Probability of Default ($PD$)** as the model prediction:
* **Ground-Truth Binary Definition ($Y_i$):**
  $$Y_i = \begin{cases} 
  1, & \text{if applicant } i \text{ defaults (defined as 90+ days past due or chargeback failure)} \\ 
  0, & \text{if applicant } i \text{ successfully settles the loan on schedule} 
  \end{cases}$$
* **Continuous Probability Output ($\hat{p}_i$):**
  $$\hat{p}_i = P(Y_i = 1 \mid \mathbf{X}_i) = \sigma(f(\mathbf{X}_i)) \in [0, 1]$$
* **Cost-Sensitive Decision Cutoff ($p_{\text{cutoff}}$):**  
  In credit scoring, misclassifying a defaulter as creditworthy (False Negative) causes immediate capital loss ($C_{\text{FN}}$), whereas misclassifying a creditworthy applicant as a defaulter (False Positive) results only in forgone interest revenue ($C_{\text{FP}}$). Therefore:
  $$C_{\text{FN}} \gg C_{\text{FP}}$$
  The optimal decision threshold $p_{\text{cutoff}}$ is derived analytically from the cost ratio and the Bank of Namibia's baseline individual default rate ($4.3\%$):
  $$p_{\text{cutoff}} = \frac{C_{\text{FP}}}{C_{\text{FP}} + C_{\text{FN}}}$$
  Applicants with $\hat{p}_i < p_{\text{cutoff}}$ are approved; those with $\hat{p}_i \ge p_{\text{cutoff}}$ are flagged as high-risk and denied credit or routed for secondary manual review.

---

## 2. Comprehensive Data Dictionary (28 Evaluated Variables)

Each candidate variable has been thoroughly evaluated across all six mandatory criteria:
1. **Why it predicts credit risk** (theoretical/empirical rationale)
2. **Legal and ethical appropriateness** (Namibian Constitution, NAMFISA, BoN)
3. **Expected data type**
4. **Expected missingness and imputation**
5. **Possible bias / proxy discrimination risks**
6. **Final model inclusion decision**

---

### Category A: Alternative Digital & Mobile Telecommunications Features (6 Variables)

#### 1. `airtime_recharge_frequency`
* **Predictive Rationale:** High and consistent recharge frequency reflects stable liquidity, daily disposable cash flow, and routine behavioral discipline (Björkegren & Grissen, 2020).
* **Legal/Ethical Appropriateness:** Fully appropriate; non-invasive behavioral summary derived from standard telco billing logs with user consent.
* **Data Type:** Continuous (Float; recharges per month).
* **Expected Missingness:** Low (<1.0%); median imputation.
* **Possible Bias:** May slightly penalize rural subsistence farmers who purchase large single vouchers seasonally; mitigate through seasonal normalization.
* **Model Decision:** `[INCLUDED]` (Primary alternative signal).

#### 2. `airtime_recharge_volatility`
* **Predictive Rationale:** Erratic fluctuations in voucher purchase amounts indicate cash flow instability and income shocks, strongly correlated with default likelihood.
* **Legal/Ethical Appropriateness:** Fully appropriate; objective statistical variance metric.
* **Data Type:** Continuous (Float; coefficient of variation).
* **Expected Missingness:** Low (<2.0%); imputed with median.
* **Possible Bias:** Minimal direct socio-economic bias.
* **Model Decision:** `[INCLUDED]`.

#### 3. `mobile_wallet_txn_regularity`
* **Predictive Rationale:** Regular, predictable weekly transaction outflow schedules serve as a direct proxy for recurring business activity or personal budgeting discipline.
* **Legal/Ethical Appropriateness:** Fully appropriate under BoN Fintech Sandbox consent guidelines.
* **Data Type:** Continuous (Normalized index $0.0 - 1.0$).
* **Expected Missingness:** Low (<1.0%); zero-fill or median.
* **Possible Bias:** Dependent on mobile wallet agent network coverage; rural users may have fewer transactions.
* **Model Decision:** `[INCLUDED]`.

#### 4. `p2p_transfer_in_out_ratio`
* **Predictive Rationale:** Net receivers of funds indicate informal remittances or merchant revenue; high outbound draining without replenishment signals insolvency.
* **Legal/Ethical Appropriateness:** Highly appropriate financial velocity measure.
* **Data Type:** Continuous (Float ratio).
* **Expected Missingness:** Low (<3.0%); bounded at $[0, 10]$.
* **Possible Bias:** Remittance-dependent households might show high ratios; valid economic signal.
* **Model Decision:** `[INCLUDED]`.

#### 5. `utility_bill_payment_consistency`
* **Predictive Rationale:** Routine payment of municipal electricity (e.g., NamPower / City of Windhoek) or water bills demonstrates debt-servicing willingness and forward financial planning.
* **Legal/Ethical Appropriateness:** Standard credit bureau substitute; highly defensible.
* **Data Type:** Continuous (Percentage $0.0 - 1.0$).
* **Expected Missingness:** Moderate (~15% due to prepaid electricity / communal water); flag missingness explicitly with indicator variable.
* **Possible Bias:** Rural or informal settlement residents lacking formal utility connections would suffer missingness. Must not automatically assign high default risk to missing utility records.
* **Model Decision:** `[INCLUDED]` (with missingness indicator).

#### 6. `account_age_telecom`
* **Predictive Rationale:** Account longevity indicates socio-economic stability and lower identity churn; fly-by-night or fraudulent borrowers frequently use newly registered SIMs.
* **Legal/Ethical Appropriateness:** Legally sound under CRAN SIM-registration regulations in Namibia.
* **Data Type:** Integer (Months).
* **Expected Missingness:** Zero (<0.1%).
* **Possible Bias:** Newer mobile subscribers (young adults or recently relocated individuals) may receive slightly lower baseline tenure points.
* **Model Decision:** `[INCLUDED]`.

---

### Category B: Micro-Enterprise & Informal Business Characteristics (8 Variables)

#### 7. `business_type`
* **Predictive Rationale:** Cash-flow cyclicity varies drastically between street vending (daily cash) and agriculture (seasonal crop/livestock sales).
* **Legal/Ethical Appropriateness:** Standard business underwriting factor.
* **Data Type:** Categorical (Nominal: Retail, Service, Agriculture, Artisan, Street Merchant).
* **Expected Missingness:** Low (<2.0%); imputed as "General/Other".
* **Possible Bias:** Risk of redlining specific informal sectors; ensure balanced weight through cross-validation.
* **Model Decision:** `[INCLUDED]`.

#### 8. `years_in_operation`
* **Predictive Rationale:** Empirical SME literature (Beck & Demirguc-Kunt, 2006) shows business survival rates jump substantially after 2–3 years; older informal businesses have stabilized client bases.
* **Legal/Ethical Appropriateness:** Fully appropriate.
* **Data Type:** Continuous (Years).
* **Expected Missingness:** Low (<3.0%); median imputation.
* **Possible Bias:** Disadvantages younger entrepreneurs; balanced with transaction velocity.
* **Model Decision:** `[INCLUDED]`.

#### 9. `monthly_revenue_estimated`
* **Predictive Rationale:** Determines debt capacity and debt-service coverage ratio (DSCR).
* **Legal/Ethical Appropriateness:** Mandatory under NAMFISA Microlending Act 2018 affordability assessment regulations.
* **Data Type:** Continuous (Monetary N$).
* **Expected Missingness:** Moderate (~10%–15% in informal self-reports); robust median by business type.
* **Possible Bias:** Self-reporting bias; verify against digital wallet inflows.
* **Model Decision:** `[INCLUDED]`.

#### 10. `monthly_operating_expenses`
* **Predictive Rationale:** High overhead relative to turnover restricts residual free cash flow available to service loans.
* **Legal/Ethical Appropriateness:** Mandatory for reckless lending prevention.
* **Data Type:** Continuous (Monetary N$).
* **Expected Missingness:** Moderate (~12%); imputed using sectoral expense ratios.
* **Possible Bias:** Informal merchants often blend domestic and enterprise expenses.
* **Model Decision:** `[INCLUDED]`.

#### 11. `net_disposable_cashflow`
* **Predictive Rationale:** Primary determinant of repayment ability; negative or razor-thin cash flow guarantees eventual default upon minor external shock.
* **Legal/Ethical Appropriateness:** Fully compliant and economically essential.
* **Data Type:** Continuous (Monetary N$: `monthly_revenue` - `monthly_expenses`).
* **Expected Missingness:** Derived feature (missing if revenue or expense missing).
* **Possible Bias:** Reflects true economic affordability.
* **Model Decision:** `[INCLUDED]`.

#### 12. `business_registration_status`
* **Predictive Rationale:** Formal businesses have greater legal recourse and stability, but informal businesses constitute 57.7% of Namibian employment.
* **Legal/Ethical Appropriateness:** Highly sensitive in financial inclusion.
* **Data Type:** Binary (`0` = Informal/Unregistered, `1` = Formal/BIPA Registered).
* **Expected Missingness:** Zero.
* **Possible Bias:** **High structural bias**. Penalizing informal businesses solely for being unregistered would defeat the entire purpose of the financial inclusion mandate in Namibia.
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Retained strictly to audit whether the model penalizes informal enterprises unfairly).

#### 13. `financial_record_availability`
* **Predictive Rationale:** Maintaining some form of record (even a physical notebook) correlates with managerial competence and lower default risk.
* **Legal/Ethical Appropriateness:** Legally sound and constructive.
* **Data Type:** Categorical (Ordinal: 0 = None, 1 = Paper Ledger, 2 = Digital Records).
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Correlated with basic literacy and education.
* **Model Decision:** `[INCLUDED]`.

#### 14. `number_of_employees`
* **Predictive Rationale:** Micro-enterprises with 1–4 employees show greater enterprise stability than solo survivalist traders.
* **Legal/Ethical Appropriateness:** Standard underwriting variable.
* **Data Type:** Integer.
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** Solo women street traders dominate informal retail; could penalize single-person operations.
* **Model Decision:** `[INCLUDED]`.

---

### Category C: Loan Facility & Credit Terms Features (4 Variables)

#### 15. `loan_amount_requested`
* **Predictive Rationale:** Larger loan amounts increase debt burden and monthly installment pressure, elevating default risk if mismatched with income.
* **Legal/Ethical Appropriateness:** Universal credit underwriting feature.
* **Data Type:** Continuous (Monetary N$: typical range N\$100 to N\$5,000 for digital microlending).
* **Expected Missingness:** Zero (Mandatory input at application).
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 16. `loan_tenor_months`
* **Predictive Rationale:** Longer tenors extend default exposure over time; digital loans typically run 1 to 6 months.
* **Legal/Ethical Appropriateness:** Standard facility term.
* **Data Type:** Integer (e.g., 1, 3, 6, 12 months).
* **Expected Missingness:** Zero.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 17. `loan_purpose`
* **Predictive Rationale:** Productive loans (inventory, equipment) generate cash returns to service debt; consumption loans (emergencies) rely on existing fixed income.
* **Legal/Ethical Appropriateness:** Standard KYC and credit appraisal field.
* **Data Type:** Categorical (Working Capital, Equipment, Inventory, Personal Emergency).
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Emergency personal loans are often required by lower-income households.
* **Model Decision:** `[INCLUDED]`.

#### 18. `installment_to_income_ratio`
* **Predictive Rationale:** The classic Debt-Service Ratio; ratios exceeding 30%–40% trigger sharp non-linear increases in default probability.
* **Legal/Ethical Appropriateness:** Legally mandatory under NAMFISA Microlending Act 2018 affordability caps.
* **Data Type:** Continuous (Ratio).
* **Expected Missingness:** Derived feature; bounded.
* **Possible Bias:** None; objective economic capacity metric.
* **Model Decision:** `[INCLUDED]`.

---

### Category D: Historical Borrowing & Savings Discipline (4 Variables)

#### 19. `number_of_previous_loans`
* **Predictive Rationale:** Established borrowing history provides track record; zero previous loans indicates thin-file status.
* **Legal/Ethical Appropriateness:** Fully appropriate.
* **Data Type:** Integer.
* **Expected Missingness:** Zero.
* **Possible Bias:** Penalizes first-time borrowers unless offset by alternative digital signals.
* **Model Decision:** `[INCLUDED]`.

#### 20. `number_of_late_payments`
* **Predictive Rationale:** Past repayment behavior is empirically the single strongest predictor of future credit performance.
* **Legal/Ethical Appropriateness:** Core credit underwriting criterion.
* **Data Type:** Integer.
* **Expected Missingness:** Zero (defaults to 0 for thin-file).
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 21. `historical_default_count`
* **Predictive Rationale:** Past un-remedied defaults demonstrate severe credit risk.
* **Legal/Ethical Appropriateness:** Universally recognized credit metric.
* **Data Type:** Integer.
* **Expected Missingness:** Zero.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

#### 22. `savings_deposit_frequency`
* **Predictive Rationale:** Active participation in formal bank savings or informal savings groups (*stokvels* / rotating funds) demonstrates financial cushion and deferred consumption discipline.
* **Legal/Ethical Appropriateness:** Highly positive financial inclusion signal.
* **Data Type:** Integer (Deposits/month).
* **Expected Missingness:** Moderate (~10%); zero-fill.
* **Possible Bias:** None.
* **Model Decision:** `[INCLUDED]`.

---

### Category E: Behavioral & Customer Interaction Data (2 Variables)

#### 23. `digital_payment_adoption_ratio`
* **Predictive Rationale:** Borrowers who actively use digital rails for payments generate richer data and exhibit higher technological fluency, correlated with modern business resilience.
* **Legal/Ethical Appropriateness:** Legally sound under digital economy policies.
* **Data Type:** Continuous (Ratio $0.0 - 1.0$).
* **Expected Missingness:** Low (<2.0%).
* **Possible Bias:** Skews towards urban centers with high merchant POS/QR adoption.
* **Model Decision:** `[INCLUDED]`.

#### 24. `dispute_complaints_count`
* **Predictive Rationale:** Frequent disputes may indicate dissatisfaction, service interruption, or contested fraudulent transactions.
* **Legal/Ethical Appropriateness:** **Ethical Risk**. Consumers must never be penalized or receive credit downgrades for exercising legitimate consumer recourse rights.
* **Data Type:** Integer.
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** High risk of penalizing assertive consumers; direct violation of Bank of Namibia consumer protection guidelines.
* **Model Decision:** `[EXCLUDED]` (Excluded entirely on ethical and consumer-rights grounds).

---

### Category F: Protected Demographic Attributes & Fairness Auditing (4 Variables)

#### 25. `applicant_age`
* **Predictive Rationale:** Correlates with career stability, financial maturity, and lifecycle consumption.
* **Legal/Ethical Appropriateness:** Permissible for age-of-majority validation; restricted against ageist discrimination.
* **Data Type:** Integer (Years, $18 - 75$).
* **Expected Missingness:** Zero.
* **Possible Bias:** Younger borrowers have shorter histories; elderly borrowers face fixed income constraints.
* **Model Decision:** `[INCLUDED_WITH_FAIRNESS_CHECKS]` (Included for non-linear lifecycle modeling; audited across age brackets: 18–25, 26–45, 46+).

#### 26. `gender`
* **Predictive Rationale:** Empirical literature (Suri & Jack, 2016) shows female informal entrepreneurs in Africa often have lower default rates.
* **Legal/Ethical Appropriateness:** **Strictly Prohibited under Article 10 of the Namibian Constitution (Equality and Freedom from Discrimination)** as a direct basis for denying credit.
* **Data Type:** Binary (`0` = Male, `1` = Female).
* **Expected Missingness:** Zero.
* **Possible Bias:** Direct gender discrimination risk.
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Strictly excluded from model input features $\mathbf{X}$; retained strictly in validation set to compute Disparate Impact Ratio and Equal Opportunity Difference).

#### 27. `location_region`
* **Predictive Rationale:** Regional macroeconomic activity and drought susceptibility influence repayment.
* **Legal/Ethical Appropriateness:** High risk of geographic redlining.
* **Data Type:** Categorical (14 Administrative Regions of Namibia).
* **Expected Missingness:** Zero.
* **Possible Bias:** High risk of acting as a proxy for ethnic enclaves or rural marginalization (violating Namibian Constitution Art. 10).
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Excluded from direct scoring; aggregated into `urban_rural` macro indicator only for fairness audits).

#### 28. `urban_rural`
* **Predictive Rationale:** Rural communities face higher infrastructural and liquidity constraints (NSA reports 27.1% rural exclusion vs 17.5% urban).
* **Legal/Ethical Appropriateness:** Sensitive attribute.
* **Data Type:** Binary (`0` = Rural/Informal, `1` = Urban).
* **Expected Missingness:** Low (<1.0%).
* **Possible Bias:** Using urban/rural as a direct rejection factor would entrench regional underdevelopment and violate the Financial Sector Transformation Strategy 2025–2035.
* **Model Decision:** `[EXCLUDED_FROM_TRAINING / RETAINED_FAIRNESS_ONLY]` (Retained strictly as a protected attribute for group fairness auditing).

---

## 3. Governance Summary

```
Total Candidate Variables Investigated: 28
├── Direct Predictive Features (X in Training Set): 23
├── Protected Attributes (Retained for Fairness Audits Only): 4
│   ├── gender
│   ├── location_region
│   ├── urban_rural
│   └── business_registration_status
└── Excluded Variables (Discarded on Ethical Grounds): 1
    └── dispute_complaints_count
```

This strict architectural separation prevents **proxy discrimination and intentional/unintentional bias**, while guaranteeing that the thesis has the exact data fields needed to run comprehensive **Demographic Parity** and **Equal Opportunity** audits in Stage 12.

With Stage 6 approved, we are positioned to proceed to **STAGE 7: Build the data-processing pipeline**.
