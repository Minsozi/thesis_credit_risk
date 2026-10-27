# Stage 5: Recommended Dataset Strategy Report

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Institution:** Department of Computer Science, University of Namibia  
**Focus:** The Triangulated Multi-Tier Dataset Strategy (Architecture, Operationalization, and Academic Defense)  

---

## 1. Executive Recommendation

Following the thorough candidate investigation in Stage 3 and the multi-criteria gap analysis in Stage 4, this report formally recommends:

> **The Triangulated Multi-Tier Research Dataset Strategy (Option 4)**  
> An integrated, three-tier framework that combines **real-world empirical digital credit transaction data**, **authentic Namibian central bank and survey statistics**, and a **fully documented, parameter-driven regulatory sandbox prototype**.

This strategy provides the thesis with complete academic defensibility. It eliminates the risk of data fabrication, overcomes the unavailability of proprietary Namibian bank/telco loan ledgers, and guarantees that all five secondary research questions (SRQs)—from algorithmic discrimination to TreeSHAP explainability, demographic fairness audits, and Bank of Namibia Regulatory Sandbox compliance—are rigorously addressed.

---

## 2. Technical Architecture & Operationalization of the Three Tiers

The strategy operates across three clearly demarcated tiers. Under no circumstances are disparate datasets secretly concatenated into a single noisy file. Instead, each tier performs a defined, transparent role within the overall research workflow.

```
+-----------------------------------------------------------------------------------+
|              TIER 1: REAL-WORLD EMPIRICAL BENCHMARK ENGINE                         |
|  - Real African Digital Transaction & Loan Ledger (Zindi Standard Bank / Xente)    |
|  - Supplementary Thin-File Lending Benchmark (Home Credit Default Risk)           |
|  Role: Powers feature extraction, ML training (Logit, DT, RF, XGBoost),           |
|        discrimination metrics (ROC-AUC, PR-AUC, FNR), and TreeSHAP explainability. |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|         TIER 2: AUTHENTIC NAMIBIAN EMPIRICAL CALIBRATION (NSA & BoN)              |
|  - Bank of Namibia Financial Stability Reports (2024, 2026b)                      |
|  - Namibia Financial Inclusion Survey (NFIS 2017 Microdata, NSA)                  |
|  - Namibia Financial Sector Transformation Strategy (NFSTS 2025-2035)             |
|  Role: Provides empirical calibration parameters:                                 |
|        * Baseline NPL Default Rate: 4.3% (Dec 2025) / 5.9% (2023)                  |
|        * Informal Economy Size: 24.7% of GDP / 57.7% of Total Employment           |
|        * Demographic Splits: 27.1% Rural Exclusion vs 17.5% Urban Exclusion        |
|        * Sets probability cutoff threshold p_cutoff and weights for fairness audits|
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|       TIER 3: DOCUMENTED BANK OF NAMIBIA REGULATORY SANDBOX PROTOTYPE             |
|  - Replicating the real-world Tamba Maris Microlending Pilot (MTC & Letshego 2025)|
|  - Microloans of N$100 - N$1,500 via mobile wallet (Maris / eWallet)              |
|  Role: Transparent, reproducible simulation testbed demonstrating the ADCAI       |
|        pipeline under the BoN Revised Fintech Regulatory Framework 2026 covenants.|
+-----------------------------------------------------------------------------------+
```

---

### Tier 1: Real-World Empirical Benchmark Engine
* **Selected Primary Dataset:** *Standard Bank / Xente Digital Financial Services Dataset* (Zindi Africa).
  * **Sample Size:** 95,662 transactions across 4,200 unique accounts.
  * **Core Features:** High-frequency transaction logs across airtime top-ups, utility bill payments, data bundles, and peer-to-peer mobile wallet transfers, accompanied by transaction start times, product categories, and amounts.
  * **Ground Truth:** Real-world default / failed settlement flag ($Y \in \{0, 1\}$).
* **Selected Supplementary Benchmark:** *Home Credit Default Risk (Application Split)* (Kaggle).
  * **Sample Size:** 307,511 applicant records.
  * **Core Features:** External alternative telecommunications and transactional credit scores (`EXT_SOURCE_1, 2, 3`), financial ratios, and explicit protected demographic attributes (`CODE_GENDER`, `DAYS_BIRTH`, `NAME_EDUCATION_TYPE`).
* **Operational Execution:**
  1. Transforms raw transactional time-series into predictive behavioral aggregates: **transaction regularity**, **airtime recharge frequency**, **spending volatility**, and **ratio of peer-to-peer transfers to bill payments**.
  2. Trains the four required machine learning models: **Logistic Regression** (baseline scorecard), **Decision Tree** (interpretable rule benchmark), **Random Forest** (bagging ensemble), and **XGBoost** (gradient boosting).
  3. Evaluates models on the holdout test set using **ROC-AUC, PR-AUC, Confusion Matrix, Brier Score Calibration, and False Negative Rate (FNR)**.
  4. Generates **TreeSHAP** global feature importances, dependence plots, and local **LIME** adverse-action decision codes.

---

### Tier 2: Authentic Namibian Empirical Calibration
Rather than making arbitrary assumptions regarding credit risk in Namibia, Tier 2 calibrates the decision parameters against official national statistics published by the Bank of Namibia and the Namibia Statistics Agency:
1. **Empirical Baseline Default Rate:** The Bank of Namibia Financial Stability Report (April 2026b) establishes that the national banking non-performing loan (NPL) ratio declined to **4.3% by December 2025** (down from **5.9% in 2023**), with individuals representing **60.2% of total default volume**. This sets the empirical prior default distribution:
   $$P(\text{Default}) \in [0.043, 0.059]$$
2. **Informal Sector Economic Reality:** Bank of Namibia Annual Reports (2026a) establish that the informal sector contributes **24.7% to national GDP** and **57.7% of total employment**, characterized by undocumented cash flows.
3. **Financial Exclusion Distribution:** The Namibia Financial Inclusion Survey (NSA, 2017) provides exact empirical demographic proportions:
   * Rural financial exclusion: **27.1%** vs. Urban exclusion: **17.5%**.
   * Non-borrowers: **57.9%** (of which **95.1%** cite fear of debt).
   * Informal safety-net reliance: **61.5%** turn to family/friends for liquidity.
4. **Calibration Application:**
   * **Cutoff Threshold Calibration ($p_{\text{cutoff}}$):** In financial inclusion, defaulting to an uncalibrated threshold of $p = 0.50$ is unacceptable. The decision cutoff is calibrated using the Namibian baseline default rate and asymmetric misclassification costs ($C_{FN} \gg C_{FP}$) to balance portfolio safety with financial deepening.
   * **Fairness Subgroup Proportions:** Protected group splits (e.g., rural vs. urban borrowers, female vs. male entrepreneurs) are weighted according to NSA NFIS 2017 microdata distributions to ensure fairness metrics (Disparate Impact Ratio, Equal Opportunity Difference) reflect genuine Namibian population structures.

---

### Tier 3: Documented Bank of Namibia Regulatory Sandbox Prototype
To demonstrate how the ADCAI framework functions in practice within the Namibian financial architecture, Tier 3 constructs a transparent, reproducible simulation testbed modeled on the real-world **Tamba Maris microlending pilot**:
* **Institutional Precedent:** In 2025, MTC Namibia partnered with Letshego Micro Financial Services to pilot *Tamba Maris*, an automated USSD/mobile-money microlending platform offering unsecured short-term credit of **N\$100 to N\$1,500** evaluated through MTC Maris wallet activity. The pilot operates inside the joint Bank of Namibia / NAMFISA Regulatory Sandbox (TechAfrica News, 2025).
* **Operational Execution:**
  1. A synthetic cohort of 5,000 thin-file applicants is generated strictly following the empirical distributions established in Tier 2 (loan requests ranging N\$100–N\$1,500, realistic airtime recharge cadences in N\$, and regional demographics matching NSA NFIS 2017).
  2. The pipeline trains the calibrated machine learning framework, applies the cost-sensitive decision cutoff, generates adverse-action reason codes via TreeSHAP, and runs demographic parity and equal opportunity audits.
  3. The simulation is stress-tested against the Bank of Namibia's **Revised Fintech Innovation Regulatory Framework 2026 Sandbox Covenants** (measuring capital at risk, consumer disclosure compliance, and default drift over a simulated 6-to-18-month testing lifecycle).
* **Ethical Declaration:** Every synthetic observation is explicitly labeled as a simulation for sandbox validation, ensuring complete academic honesty and zero data misrepresentation.

---

## 3. Academic Defense & Viva Voce Strategy

When defending this thesis before an examination committee at the University of Namibia, the candidate will defend this dataset strategy using four decisive arguments:

1. **Strict Adherence to Research Ethics & Non-Fabrication:**  
   *Claim:* The candidate explicitly acknowledges that real Namibian borrower-level transaction files are protected by banking secrecy and telco privacy laws. Attempting to disguise simulated data as "scraped" or "confidential bank data" would constitute academic misconduct. The triangulated approach maintains 100% academic integrity.
2. **Empirical Validity of the Machine Learning Engine:**  
   *Claim:* The core algorithms (Logistic Regression, Decision Tree, Random Forest, XGBoost) and explainability tools (TreeSHAP) are evaluated on genuine, high-volume digital financial services transactions with true default labels (Tier 1), proving that the behavioral signals and non-linear interactions are mathematically real.
3. **Institutional and Sovereign Grounding:**  
   *Claim:* Rather than leaving the research as an abstract foreign case study, Tier 2 and Tier 3 calibrate the model directly to the Bank of Namibia's 4.3% NPL benchmark, the NSA's 27.1% rural exclusion reality, and the *Tamba Maris* regulatory sandbox lifecycle.
4. **Policy Impact for Namibia:**  
   *Claim:* The research produces an immediate, practical contribution: a regulatory-compliant blueprint that fintechs and digital lenders can submit directly to the Bank of Namibia Regulatory Sandbox under the *Revised Fintech Framework 2026* and the *Financial Sector Transformation Strategy 2025–2035*.

---

## 4. Next Steps & Transition to Stage 6

With the dataset strategy formally established and approved, the next operational milestone is:
> **STAGE 6: Build the Data Dictionary**  
> Formulate the comprehensive credit-risk data dictionary detailing all candidate features across financial, behavioral, alternative, and protected demographic dimensions, specifying predictive rationale, legal/ethical appropriateness, expected missingness, and proxy bias risks.
