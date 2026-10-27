# UNIVERSITY OF NAMIBIA
## FACULTY OF AGRICULTURE, ENGINEERING & NATURAL SCIENCES
### DEPARTMENT OF COMPUTING, MATHEMATICAL AND STATISTICAL SCIENCE

---

# CREDIT RISK PREDICTION FOR FINANCIAL INCLUSION USING MACHINE LEARNING IN NAMIBIA: AN EMPIRICAL AND SOCIO-TECHNICAL INVESTIGATION UNDER THE BANK OF NAMIBIA FINTECH REGULATORY FRAMEWORK

A thesis submitted in partial fulfilment of the requirements for the degree of  
**Bachelor of Science in Computer Science (Honours)**

**Student Name:** Percyviarance Minsozi Simasiku  
**Student Number:** 201061589  
**Supervisor:** Mrs. Johanna Nelulu  
**Date:** October, 2026  

---

<div style="page-break-after: always;"></div>

## DECLARATION

I, **Percyviarance Minsozi Simasiku**, declare that this thesis is my original work and has not been submitted to any other institution for the award of a degree. All sources used in this study have been appropriately acknowledged.

\
\
Signature: ______________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: ______________________________

---

<div style="page-break-after: always;"></div>

## ABSTRACT

In Namibia, over $77\%$ of the adult population remains excluded from formal credit markets due to a lack of legacy banking histories, collateral, and formalized financial documentation—a condition known as the "thin-file" exclusion paradox. Traditional linear credit scorecards rely strictly on historical credit bureau telemetry, systematically locking out unbanked informal entrepreneurs, rural smallholders, and youth. This study investigates the extent to which machine learning algorithms leveraging non-traditional mobile transactional and behavioral telemetry (e.g., airtime recharge regularity, mobile wallet velocity, and telecom account tenure) can predict credit default risk accurately, transparently, and fairly for thin-file borrowers, while complying with the *Bank of Namibia (BoN) Revised Fintech Innovation Regulatory Framework (2026)* and the *National Financial Sector Transformation Strategy (NFSTS 2025–2035)*.

Adopting a Triangulated Multi-Tier Dataset Strategy, an empirical cohort of $N = 5,000$ micro-borrowers was generated and conditioned on authentic African digital credit distributions, calibrated to the Bank of Namibia December 2025 Non-Performing Loan benchmark of $3.93\%$, and constrained to the micro-loan mechanics ($N\$100 - N\$1,500$, $30$-day tenure) of the BoN Sandbox pilot. Four predictive algorithms—Logistic Regression, Decision Trees, Random Forest, and XGBoost—were engineered, cross-validated, benchmarked via paired DeLong statistical tests, explained using TreeSHAP, and audited for algorithmic bias across constitutional protected attributes.

Empirical findings reveal that alternative behavioral indicators provide statistically significant discriminatory signal ($p < 0.001$), with mobile telecom tenure, airtime recharge stability, and recharge frequency accounting for $54.6\%$ of total predictive importance mass. Random Forest achieved superior probability calibration (**Brier Score = 0.0997**, cutting error by $50.6\%$ relative to Logistic Regression) and minimized portfolio default loss to $298.0$ under an asymmetric cost matrix ($C_{FN}=5, C_{FP}=1$). TreeSHAP local attributions successfully eliminated the "black-box" dilemma, generating compliant individual adverse-action explanation notices that satisfy BoN Framework Section 5.1. The algorithmic fairness audit proved that XGBoost naturally satisfies the international four-fifths rule ($DIR \ge 0.80$) across gender ($DIR = 1.1413$), geographic location ($DIR = 0.9513$), and business registration ($DIR = 1.3127$) without post-hoc distortion. The study articulates the Calibration–Fairness–Inclusion Trilemma, advancing eight actionable policy recommendations to govern digital credit deployment in Namibia.

**Keywords:** Credit Risk Prediction; Financial Inclusion; Machine Learning; Alternative Data; TreeSHAP; Algorithmic Fairness; Bank of Namibia Regulatory Sandbox.

---

<div style="page-break-after: always;"></div>

## ACKNOWLEDGEMENTS

First and foremost, I express my deepest gratitude to Almighty God for granting me wisdom, strength, perseverance, and good health throughout the duration of this research.

I extend my profound appreciation and heartfelt gratitude to my academic supervisor, **Mrs. Johanna Nelulu**, Department of Computing, Mathematical and Statistical Science, University of Namibia. Her invaluable mentorship, rigorous academic critique, insightful guidance, and continuous encouragement shaped the direction and execution of this dissertation.

I also extend sincere appreciation to the academic and administrative staff of the Faculty of Agriculture, Engineering and Natural Sciences at UNAM for their dedicated teaching and support throughout my undergraduate studies.

Special recognition is accorded to the **Bank of Namibia (BoN)** for their public dissemination of the *Revised Fintech Innovation Regulatory Framework (2026)* and macroeconomic banking supervision statistics, and to the **Namibia Statistics Agency (NSA)** for publishing comprehensive financial inclusion microdata via the *National Financial Inclusion Survey (NFIS)*.

Finally, I am profoundly indebted to my family and friends for their boundless patience, emotional sustenance, and faith in my abilities during long hours of research, programming, and writing.

---

<div style="page-break-after: always;"></div>

## DEDICATION (OPTIONAL)

This thesis is dedicated to my family, whose continuous sacrifices, unconditional love, and prayers have been my foundation; and to the hardworking micro-entrepreneurs, informal traders, and rural households of Namibia, whose economic vitality drives our nation forward despite enduring financial exclusion.

---

<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

- **DECLARATION**
- **ABSTRACT**
- **ACKNOWLEDGEMENTS**
- **DEDICATION**
- **TABLE OF CONTENTS**
- **LIST OF FIGURES**
- **LIST OF TABLES**
- **LIST OF ABBREVIATIONS AND ACRONYMS**
- **CHAPTER 1: INTRODUCTION**
  - 1.1 Introduction
  - 1.2 Background of the Study
  - 1.3 Problem Statement
  - 1.4 Aim of the Study
  - 1.5 Research Objectives
  - 1.6 Research Questions
  - 1.7 Significance of the Study
  - 1.8 Scope of the Study
  - 1.9 Limitations of the Study
- **CHAPTER 2: LITERATURE REVIEW**
  - 2.1 Introduction
  - 2.2 Theoretical Background
  - 2.3 Conceptual Framework
  - 2.4 Review of Existing Technologies
  - 2.5 Review of Related Studies
  - 2.6 Review of Existing Systems or Applications
  - 2.7 Research Gap
  - 2.8 Summary of the Chapter
- **CHAPTER 3: RESEARCH METHODOLOGY**
  - 3.1 Introduction
  - 3.2 Research Approach
  - 3.3 Research Design
  - 3.4 Target Population
  - 3.5 Sampling Techniques and Sample Size
  - 3.6 Data Collection Methods
  - 3.7 Data Analysis Methods
  - 3.8 Software Development Methodology
  - 3.9 Ethical Considerations
  - 3.10 Chapter Summary
- **CHAPTER 4: SYSTEM ANALYSIS AND DESIGN**
  - 4.1 Introduction
  - 4.2 Analysis of the Existing System
    - 4.2.1 Functional Requirements
    - 4.2.2 Non-Functional Requirements
  - 4.3 System Design
  - 4.4 Database Design
  - 4.5 User Interface Design
  - 4.6 System Architecture
- **CHAPTER 5: SYSTEM IMPLEMENTATION**
  - 5.1 Introduction
  - 5.2 Development Environment
  - 5.3 System Implementation
  - 5.4 Implementation of Major Features
  - 5.5 Database Implementation
  - 5.6 Security Implementation
  - 5.7 Challenges Encountered During Development
- **CHAPTER 6: SYSTEM TESTING AND EVALUATION**
  - 6.1 Introduction
  - 6.2 Testing Strategy
  - 6.3 Test Cases
  - 6.4 Testing Results
  - 6.5 System Evaluation
  - 6.6 User Feedback and Usability Evaluation
  - 6.7 Discussion of Findings
- **CHAPTER 7: CONCLUSION AND RECOMMENDATIONS**
  - 7.1 Introduction
  - 7.2 Summary of the Study
  - 7.3 Summary of Key Findings
  - 7.4 Achievement of Research Objectives
  - 7.5 Conclusion
  - 7.6 Recommendations
  - 7.7 Suggestions for Future Research
- **REFERENCES**
- **APPENDICES**

---

<div style="page-break-after: always;"></div>

## LIST OF FIGURES

- Figure 2.1: Conceptual Architecture of the Alternative Data Scoring Framework
- Figure 3.1: Triangulated Multi-Tier Dataset Architecture Pipeline
- Figure 4.1: End-to-End System Architecture of the Credit Risk Prototype
- Figure 4.2: Nokia 3310 USSD Mobile Interface Wireframe (*140*555#)
- Figure 6.1: Receiver Operating Characteristic (ROC) Curves Across Evaluated Models
- Figure 6.2: Precision-Recall (PR) Curves under 3.93% Class Imbalance
- Figure 6.3: Probability Calibration Curves (Reliability Diagrams)
- Figure 6.4: Portfolio Financial Cost Curves (Asymmetric Loss C_FN=5, C_FP=1)
- Figure 6.5: TreeSHAP Global Feature Importance Bar Chart
- Figure 6.6: Local Adverse-Action Waterfall Decomposition for Applicant NAM-11764
- Figure 6.7: Credit Approval Rates Disaggregated by Protected Demographic Sub-Groups
- Figure 6.8: Disparate Impact Ratio (DIR) Comparison against 0.80 Four-Fifths Reference Line
- Figure 6.9: False Negative Rate Disparity Analysis across Protected Groups
- Figure 7.1: The Calibration–Fairness–Inclusion Trilemma in Emerging Market Micro-Lending

---

<div style="page-break-after: always;"></div>

## LIST OF TABLES

- Table 1.1: Alignment Matrix: Objectives, Questions, and Hypotheses
- Table 2.1: Key Empirical Studies on Alternative Data Credit Risk Modeling
- Table 2.2: Comparative Summary of Supervised Learning Algorithms in Credit Risk
- Table 3.1: Comparative Scoring Matrix of Evaluated Dataset Architectures
- Table 4.1: Functional Requirements Specification (FR1 - FR6)
- Table 4.2: Non-Functional Requirements Specification (NFR1 - NFR5)
- Table 4.3: Data Dictionary: 28 Variables across 6 Governance Dimensions
- Table 6.1: Full Benchmark Results on Holdout Test Set (N = 1,500)
- Table 6.2: Paired DeLong Statistical Significance Tests on ROC-AUC
- Table 6.3: Cost-Sensitive Operational Threshold Optimization under Asymmetric Loss
- Table 6.4: Top 15 Predictors Ranked by Mean Absolute TreeSHAP Attribution
- Table 6.5: Local Adverse-Action Decomposition for Declined Applicant NAM-11764
- Table 6.6: Algorithmic Fairness Audit: DIR and EOD across Protected Demographic Groups
- Table 7.1: Achievement of Research Objectives Evidence Matrix
- Table 7.2: Definitive Hypothesis Testing Decision Matrix (H0,1 to H0,4)

---

<div style="page-break-after: always;"></div>

## LIST OF ABBREVIATIONS AND ACRONYMS

| Acronym | Definition |
|---|---|
| **AI** | Artificial Intelligence |
| **AUC** | Area Under the Curve |
| **BoN** | Bank of Namibia |
| **CART** | Classification and Regression Trees |
| **CDR** | Call Detail Record |
| **CRAN** | Communications Regulatory Authority of Namibia |
| **CV** | Cross-Validation |
| **DIR** | Disparate Impact Ratio |
| **DPD** | Demographic Parity Difference |
| **DT** | Decision Tree |
| **EEOC** | Equal Employment Opportunity Commission (United States) |
| **EOD** | Equal Opportunity Difference |
| **FN** | False Negative |
| **FNR** | False Negative Rate |
| **FP** | False Positive |
| **FPR** | False Positive Rate |
| **GNN** | Graph Neural Network |
| **IV** | Information Value |
| **IVR** | Interactive Voice Response |
| **LIME** | Local Interpretable Model-agnostic Explanations |
| **ML** | Machine Learning |
| **MNO** | Mobile Network Operator |
| **MSME** | Micro, Small, and Medium Enterprises |
| **MTC** | Mobile Telecommunications Limited (Namibia) |
| **NAMFISA** | Namibia Financial Institutions Supervisory Authority |
| **NFIS** | National Financial Inclusion Survey (Namibia) |
| **NFSTS** | National Financial Sector Transformation Strategy (2025–2035) |
| **NPL** | Non-Performing Loan |
| **NSA** | Namibia Statistics Agency |
| **PD** | Probability of Default |
| **PR-AUC** | Precision-Recall Area Under the Curve |
| **RF** | Random Forest |
| **ROC** | Receiver Operating Characteristic |
| **SHAP** | SHapley Additive exPlanations |
| **SIM** | Subscriber Identity Module |
| **STS** | Science and Technology Studies |
| **TN** | True Negative |
| **TP** | True Positive |
| **TPR** | True Positive Rate |
| **UNAM** | University of Namibia |
| **USSD** | Unstructured Supplementary Service Data |
| **WoE** | Weight of Evidence |
| **XAI** | Explainable Artificial Intelligence |
| **XGBoost** | Extreme Gradient Boosting |

---

<div style="page-break-after: always;"></div>

# CHAPTER 1: INTRODUCTION

### 1.1 Introduction
In emerging economies, access to formal credit is universally recognized as a vital driver of micro-enterprise growth, household financial resilience, and poverty alleviation. In the Republic of Namibia, however, access to formal financial credit remains heavily skewed toward urban formal-sector wage earners, while the vast majority of informal traders, rural smallholders, and low-income citizens remain excluded. This study investigates how modern machine learning algorithms leveraging non-traditional mobile transactional and telecommunications behavioral data can overcome this credit gap accurately, transparently, and fairly within the regulatory environment established by the Bank of Namibia (BoN) Revised Fintech Innovation Regulatory Framework (2026).

### 1.2 Background of the Study
The Namibian financial sector is characterized by an acute structural dualism: a sophisticated commercial banking system coexists with an expansive, financially underserved informal economy. According to the National Financial Inclusion Survey (NFIS) conducted by the Namibia Statistics Agency (NSA, 2017), while transactional financial access has expanded through basic mobile wallets, over 77.3% of Namibian adults remain entirely excluded from formal credit. Commercial bank lending is severely restricted, with only 11.3% of rural adults and 8.6% of informal micro-enterprises possessing formal credit access.

Traditional banking institutions rely on legacy credit underwriting scorecards that mandate formal payslips, audited commercial accounting statements, registered credit bureau histories, and physical collateral (such as urban real estate). For Namibia's informal workforce—which constitutes approximately 34% of active employment—these evidentiary prerequisites represent an insurmountable barrier. Consequently, unbanked citizens are forced to rely on unregulated cash loan operators (*omashikofolas*), who exploit the liquidity void by charging usurious interest rates (30% to over 100% per month).

Simultaneously, telecommunications infrastructure has expanded rapidly. Mobile network operators—predominantly Mobile Telecommunications Limited (MTC) and Telecom Namibia (TN Mobile)—report mobile subscriber penetration rates exceeding 110% of the national population. Unbanked citizens routinely purchase airtime, transfer funds via Unstructured Supplementary Service Data (USSD), and maintain digital mobile wallets. This daily digital activity leaves fine-grained behavioral traces that econometric literature suggests encode valuable signals of creditworthiness, offering a viable path toward inclusive automated underwriting.

### 1.3 Problem Statement
The central problem investigated in this dissertation is the **"thin-file" financial exclusion paradox** in the Namibian credit market: traditional credit scoring frameworks rely strictly on historical credit bureau records and formal collateral, creating a self-reinforcing barrier that locks out creditworthy informal, rural, and low-income borrowers. While non-traditional mobile transactional data offers an empirical bridge to assess these unbanked populations, non-linear machine learning models present substantial risks of algorithmic opacity ("black-box" decisions), demographic bias across protected sub-groups (gender, geography, business formalization), and regulatory misalignment under Namibian financial sector laws.

### 1.4 Aim of the Study
The overarching aim of this research is to design, develop, benchmark, explain, and audit a machine learning-based credit risk assessment prototype utilizing alternative transactional and telecommunications data for thin-file micro-borrowers in Namibia, establishing an operational underwriting model aligned with the Bank of Namibia's Regulatory Sandbox.

### 1.5 Research Objectives
To accomplish this aim, the study pursued five specific, measurable research objectives:
1. **Objective 1:** To design and implement a leak-free data processing and feature engineering pipeline that extracts behavioral, transactional, and stability features from non-traditional mobile telemetry.
2. **Objective 2:** To train, tune, and systematically benchmark four supervised learning algorithms—Logistic Regression, Decision Trees, Random Forest, and XGBoost—across discrimination, calibration, and cost-sensitive loss.
3. **Objective 3:** To execute paired DeLong statistical significance tests on holdout ROC-AUC metrics to determine whether non-linear ensemble models statistically outperform baseline scorecards.
4. **Objective 4:** To implement TreeSHAP (SHapley Additive exPlanations) to decompose model predictions globally and locally, generating compliant adverse-action reason codes for rejected applicants.
5. **Objective 5:** To audit baseline models for disparate impact across protected demographic sub-groups (gender, urban/rural location, and business registration status) under the international four-fifths rule, evaluate threshold-based mitigation, and synthesize actionable governance guidelines.

### 1.6 Research Questions
The research addressed the following primary and secondary research questions:
* **Primary Research Question (PRQ):** To what extent can machine learning models leveraging alternative transactional and behavioral data accurately, transparently, and fairly predict credit default risk for underserved, thin-file borrowers, and how can such a framework be responsibly operationalized within Namibia's regulatory environment?
* **Secondary Research Questions (SRQs):**
  - **SRQ 1:** Which non-traditional behavioral, digital wallet, and telecom features provide statistically significant predictive signal for credit default risk in the absence of legacy credit bureau history?
  - **SRQ 2:** How do non-linear ensemble algorithms (Random Forest, XGBoost) compare against interpretable baselines (Logistic Regression, Decision Trees) in terms of discriminatory power, cost-sensitive loss, and probability calibration?
  - **SRQ 3:** Can post-hoc explainability techniques (TreeSHAP) provide faithful, case-level risk attributions that satisfy statutory adverse-action disclosure standards?
  - **SRQ 4:** Do machine learning credit risk models trained on alternative data introduce or amplify disparate impact across protected demographic sub-populations, and can fairness-constrained post-processing reduce disparate outcomes?
  - **SRQ 5:** How can the proposed alternative data credit risk framework be operationalized to comply with the testing covenants of the Bank of Namibia's Revised Fintech Innovation Regulatory Framework (2026)?

### 1.7 Significance of the Study
This dissertation delivers substantial contributions across academic, regulatory, and socio-economic domains:
* **Academic & Theoretical:** Formulates the Calibration–Fairness–Inclusion Trilemma, establishing the fundamental trade-offs between commercial probability calibration, constitutional non-discrimination, and financial inclusion volume in emerging markets.
* **Methodological:** Validates the Triangulated Multi-Tier Dataset Strategy, providing a reproducible methodology for conducting rigorous machine learning research in data-scarce emerging economies without compromising institutional secrecy.
* **Policy & Regulatory:** Provides the Bank of Namibia Fintech Supervision Unit and NAMFISA with the technical specifications, explainability templates, and fairness metrics required to draft a formal Algorithmic Credit Scoring Guidance Note.
* **Socio-Economic:** Provides the empirical foundation to expand affordable digital nano-loans to informal traders and rural smallholders, curbing dependence on predatory informal moneylenders.

### 1.8 Scope of the Study
The geographical and legal scope is bounded strictly by the Republic of Namibia. Macroeconomic default prevalence ($3.93\%$) is calibrated to Bank of Namibia December 2025 benchmarks. The credit facility modeled is an unsecured digital micro-loan ($N\$100$ to $N\$1,500$ with a fixed $30$-day single-bullet repayment tenure) matching the Tamba Maris USSD pilot in the BoN Regulatory Sandbox. Intrusive data sources (e.g., GPS trails, call recordings, social media contacts) were strictly excluded on ethical grounds.

### 1.9 Limitations of the Study
Three primary limitations are acknowledged: (1) Due to banking secrecy and privacy laws, models were trained on an empirically calibrated synthetic cohort rather than live commercial bank transaction ledgers; (2) The study focused on short-term 30-day micro-loans and does not model multi-year amortizing commercial facilities; and (3) The analysis assumed a stationary macroeconomic environment and did not incorporate dynamic multi-year drought or inflation shocks.

---

<div style="page-break-after: always;"></div>

# CHAPTER 2: LITERATURE REVIEW

### 2.1 Introduction
This chapter surveys the evolution of credit risk assessment, examines modern machine learning applications in digital microfinance, reviews the theoretical mechanisms linking alternative behavioral telemetry to creditworthiness, and evaluates computational frameworks for explainability and algorithmic fairness within the Namibian regulatory context.

### 2.2 Theoretical Background
The economic foundation of credit rationing rests on Stiglitz and Weiss's (1981) theory of asymmetric information. In credit markets, borrowers possess private information regarding their repayment integrity that lenders cannot observe directly. Raising interest rates to compensate for unobserved risk triggers adverse selection (driving away safe borrowers) and moral hazard (incentivizing risky projects). Consequently, lenders ration credit, denying loans to applicants who cannot supply formal credit bureau records or physical collateral.

### 2.3 Conceptual Framework
This study proposes a multi-dimensional conceptual framework integrating four core pillars: Alternative Behavioral Telemetry Ingestion, Supervised Machine Learning Underwriting, TreeSHAP Explainability, and Constitutional Fairness Auditing. The framework is governed by the Calibration–Fairness–Inclusion Trilemma, which formalizes the mathematical trade-offs between commercial probability calibration, constitutional non-discrimination, and credit volume expansion.

### 2.4 Review of Existing Technologies
In credit scoring literature, four supervised learning families dominate: (1) Logistic Regression scorecards, providing monotonic linear interpretability; (2) Decision Trees (CART), providing visual rule splitting but suffering from high variance; (3) Random Forest, providing bootstrap aggregation (bagging) with excellent probability calibration; and (4) XGBoost, providing gradient boosting with high discrimination on tabular data. TreeSHAP (Lundberg et al., 2020) provides polynomial-time computation of Shapley additive feature attributions for tree ensembles.

### 2.5 Review of Related Studies
Landmark empirical studies validate the predictive power of alternative data. Björkegren and Grissen (2018) analyzed prepaid mobile Call Detail Records (CDRs) and airtime top-ups in Rwanda, proving that mobile phone telemetry predicts default with accuracy comparable to traditional scorecards. Óskarsdóttir et al. (2019) demonstrated that combining telecommunications metadata with credit bureau files significantly improves discriminatory AUC. Berg et al. (2020) proved that simple digital footprints left during e-commerce transactions predict consumer default as accurately as traditional credit bureau ratings. Suri and Jack (2016) demonstrated the transformative economic welfare impact of digital mobile money access in Kenya.

### 2.6 Review of Existing Systems or Applications
Across East Africa, automated mobile lending platforms such as Safaricom/NCBA's M-Shwari, Tala, and Branch have disbursed billions in digital credit. However, ethnographic investigations (Mwesigwa et al., 2026) reveal systemic risks: excessive credit cycling, aggressive algorithmic debt collection, and credit bureau blacklisting for small micro-loan defaults. In Namibia, commercial banks remain tied to legacy branch underwriting, leaving digital micro-credit to emerging sandbox prototypes such as Tamba Maris.

### 2.7 Research Gap
Three critical research gaps were identified: (1) The absence of public empirical alternative data benchmarks calibrated to Southern African macroeconomic environments; (2) A research silo between machine learning discrimination and constitutional fairness auditing; and (3) The lack of operational frameworks translating computational models into compliance with emerging central bank sandboxes, such as the Bank of Namibia 2026 Framework.

### 2.8 Summary of the Chapter
This chapter established the theoretical and empirical foundations of alternative-data credit scoring. While mobile behavioral telemetry provides an authentic proxy for financial capacity, deploying non-linear algorithms requires resolving the dual challenges of explainability and algorithmic fairness, which are addressed in the methodology that follows.

---

<div style="page-break-after: always;"></div>

# CHAPTER 3: RESEARCH METHODOLOGY

### 3.1 Introduction
This chapter outlines the research methodology, sampling techniques, data governance rules, machine learning pipeline engineering, and statistical testing protocols utilized to investigate credit risk prediction for financial inclusion in Namibia.

### 3.2 Research Approach
The study employs a pragmatic mixed-methods sequential explanatory approach. Quantitative computational modeling serves as the primary empirical core, complemented by qualitative socio-technical and regulatory policy analysis.

### 3.3 Research Design
An experimental computational research design was implemented. Four supervised learning models were engineered, tuned using 5-fold stratified cross-validation, and benchmarked on an independent holdout test partition across discrimination, calibration, asymmetric cost loss, and fairness metrics.

### 3.4 Target Population
The target population comprises unbanked and underserved micro-borrowers in Namibia, specifically informal open-market traders, rural smallholders, and micro-enterprise operators who lack formal credit bureau files and collateral.

### 3.5 Sampling Techniques and Sample Size
A stratified sample of $N = 5,000$ applicant records was generated and split into a 70% training partition ($N = 3,500$) and a 30% holdout test partition ($N = 1,500$). Default prevalence was precisely calibrated to $3.93\%$ (matching Bank of Namibia December 2025 benchmarks). Demographic splits were stratified according to NSA NFIS 2017 statistics ($53.5\%$ female, $46.5\%$ male; $57.1\%$ urban, $42.9\%$ rural).

### 3.6 Data Collection Methods
Due to proprietary commercial banking secrecy, data was generated via the Triangulated Multi-Tier Dataset Strategy: Tier 1 anchored behavioral feature distributions to verified African digital micro-lending benchmarks; Tier 2 conditioned demographic and default distributions on official Namibian microdata; Tier 3 constrained credit mechanics to the Tamba Maris BoN sandbox pilot.

### 3.7 Data Analysis Methods
Data analysis incorporated: (1) ROC-AUC and PR-AUC for discrimination; (2) Brier Score for probability calibration; (3) Cost-sensitive asymmetric loss minimization ($C_{FN}=5, C_{FP}=1$); (4) Paired DeLong statistical tests on holdout ROC-AUC; (5) TreeSHAP for global and local explainability; and (6) Disparate Impact Ratio (DIR) and Equal Opportunity Difference (EOD) for fairness auditing.

### 3.8 Software Development Methodology
The system prototype was developed using an Agile Iterative Prototyping methodology across 15 structured research stages, culminating in serialized joblib models and an interactive Streamlit presentation application.

### 3.9 Ethical Considerations
In accordance with Article 10 of the Namibian Constitution, four protected demographic attributes (`gender`, `location_region`, `urban_rural`, and `business_registration_status`) were strictly excluded from the training feature matrix $X$ to prevent disparate treatment. The variable `dispute_complaints_count` was permanently excluded to protect consumer grievance rights.

### 3.10 Chapter Summary
This chapter specified the end-to-end methodological protocol, ensuring strict data leakage prevention, ethical feature decoupling, and statistical rigor.

---

<div style="page-break-after: always;"></div>

# CHAPTER 4: SYSTEM ANALYSIS AND DESIGN

### 4.1 Introduction
This chapter presents the system analysis and architectural design of the automated alternative-data credit scoring and explainability engine developed for the Bank of Namibia Regulatory Sandbox.

### 4.2 Analysis of the Existing System
The existing commercial banking underwriting process in Namibia is manual, paper-intensive, and reliant on legacy credit bureaus. It requires applicants to travel to physical bank branches, submit physical documentation (3 months of payslips, certified identity copies, registered business licenses), and wait 5 to 14 days for committee review. This workflow completely excludes informal traders who operate in cash and lack formal documentation.

#### 4.2.1 Functional Requirements
The system must satisfy six core functional requirements:
* **FR1 (Alternative Data Ingestion):** Ingest non-intrusive telecommunications and mobile wallet telemetry via API/USSD.
* **FR2 (Machine Learning Underwriting):** Compute calibrated default probabilities using optimized ensemble models in $< 150 \text{ ms}$.
* **FR3 (Dynamic Decisioning & Limit Allocation):** Output binary approval/decline decisions and assign risk-based credit limits ($N\$100 - N\$1,500$).
* **FR4 (Automated Adverse-Action Generation):** Decompose adverse decisions via TreeSHAP and generate human-readable reason codes.
* **FR5 (Algorithmic Fairness Monitoring):** Provide automated auditing of Disparate Impact Ratios across protected demographic groups.
* **FR6 (USSD Borrower Interaction):** Deliver an interactive, zero-rated USSD interface (`*140*555#`) for feature phone users.

#### 4.2.2 Non-Functional Requirements
* **NFR1 (Performance):** Real-time scoring latency must not exceed 150 milliseconds per request.
* **NFR2 (Calibration Reliability):** The model Brier Score must remain below 0.15 to ensure reliable loan loss provisioning.
* **NFR3 (Fairness Compliance):** Disparate Impact Ratios across gender and geography must satisfy the four-fifths rule ($DIR \ge 0.80$).
* **NFR4 (Transparency):** Adverse decisions must be explainable without requiring manual underwriter intervention.
* **NFR5 (Security & Privacy):** Zero demographic attributes may be utilized in the live feature vector $X$.

### 4.3 System Design
The system design models the interaction between the unbanked borrower, the USSD gateway, the machine learning inference engine, the TreeSHAP explainer, and the Bank of Namibia sandbox supervisory interface.

### 4.4 Database Design
The database architecture is grounded in a 28-variable data dictionary partitioned into metadata, raw behavioral telemetry, engineered financial ratios, and protected demographic audit attributes. Continuous features are winsorized at the 1st and 99th percentiles and standardized using `StandardScaler`.

### 4.5 User Interface Design
Two primary user interfaces were engineered: (1) A monochrome USSD mobile wireframe (`*140*555#`) operating within the 182-character GSM protocol constraint; and (2) A web-based loan officer and supervisory dashboard developed in Streamlit, featuring real-time risk badges, interactive input sliders, and live TreeSHAP waterfall charts.

### 4.6 System Architecture
The multi-tier system architecture comprises five decoupled layers: (1) Data Ingestion Layer; (2) Preprocessing & Leak-Free Scaling Pipeline; (3) Machine Learning Inference Engine (XGBoost/Random Forest); (4) TreeSHAP & Fairness Auditing Middleware; and (5) Presentation & USSD Gateway Layer.

---

<div style="page-break-after: always;"></div>

# CHAPTER 5: SYSTEM IMPLEMENTATION

### 5.1 Introduction
This chapter documents the technical implementation of the machine learning scoring engine, the data pipeline, the TreeSHAP explainability middleware, and the interactive presentation prototype.

### 5.2 Development Environment
The system was implemented using Python 3.11 within a virtualized Windows environment managed via the `uv` package manager. Key libraries included Scikit-Learn 1.9.1 (baselines, preprocessing, metrics), XGBoost 3.2.0 (gradient boosting), SHAP 0.51.0 (TreeSHAP attribution), Matplotlib 3.11.2 and Seaborn 0.13.2 (visualization), Joblib 1.6.0 (serialization), and Streamlit 1.64.0 (interactive UI).

### 5.3 System Implementation
The implementation is modularized across standalone scripts in the `src/` directory: `data_generation.py` (cohort simulation), `data_cleaning.py` (winsorization and missingness flags), `feature_engineering.py` (ratio construction and leak-free scaling), `train_baselines.py` (Logistic Regression and Decision Trees), `train_advanced.py` (Random Forest and XGBoost), `evaluate.py` (DeLong tests and cost optimization), `explainability.py` (TreeSHAP attributions), and `fairness_audit.py` (disparate impact testing).

### 5.4 Implementation of Major Features
Major features implemented include: (1) XGBoost loss weighting using `scale_pos_weight = 24.36` to resolve the $3.93\%$ default class imbalance; (2) TreeSHAP exact polynomial-time waterfall decomposition translating margins into log-odds risk factors; (3) Automated plain-language adverse-action SMS notice generation; and (4) An interactive Streamlit dashboard (`app.py`) launched via `launch_presentation_tool.bat`.

### 5.5 Database Implementation
Processed features and ground truth targets are persisted as structured CSV files in `data/processed/`. Trained machine learning models and fitted `StandardScaler` transformers are serialized as binary `.joblib` artifacts in `models/`.

### 5.6 Security Implementation
Security and constitutional compliance are enforced via architectural feature decoupling: demographic attributes are stored in a separate protected partition (`protected_attributes_test.csv`) and are physically inaccessible to the model inference pipeline during scoring.

### 5.7 Challenges Encountered During Development
Key technical challenges resolved during development included: (1) Extreme class imbalance ($3.93\%$ default rate), which caused standard classifiers to predict zero defaults; (2) Operator precedence errors during cost curve threshold sweeps, which were diagnosed and resolved; and (3) Windows console cp1252 character encoding conflicts with Unicode checkmarks, which were resolved via ASCII sanitization.

---

<div style="page-break-after: always;"></div>

# CHAPTER 6: SYSTEM TESTING AND EVALUATION

### 6.1 Introduction
This chapter presents the empirical testing results, statistical hypothesis tests, probability calibration diagrams, cost-sensitive portfolio loss analyses, TreeSHAP feature attributions, and algorithmic fairness audits conducted on the holdout test partition ($N = 1,500$).

### 6.2 Testing Strategy
Testing incorporated 5-fold stratified cross-validation on training data, out-of-sample holdout test benchmarking, paired DeLong statistical significance tests, and four-fifths demographic parity auditing across gender, geography, and business formalization.

### 6.3 Test Cases
Six core functional and algorithmic test cases were executed:
* **TC01 (Leak-Free Normalization):** Fit StandardScaler strictly on Train partition. Status: **PASSED**.
* **TC02 (Class Imbalance Weighting):** Set `scale_pos_weight = 24.36` in XGBoost. Default recall reached $45.76\%$. Status: **PASSED**.
* **TC03 (Probability Calibration):** Evaluate Brier Score on holdout set. Random Forest achieved $0.0997$. Status: **PASSED**.
* **TC04 (TreeSHAP Local Attribution):** Decompose adverse case `NAM-11764`. Exact additive efficiency verified ($R^2 = 1.000$). Status: **PASSED**.
* **TC05 (Gender Fairness Audit):** Evaluate DIR across Female vs Male. XGBoost achieved $DIR = 1.1413 \ge 0.80$. Status: **PASSED**.
* **TC06 (Rural Fairness Mitigation):** Audit Rural vs Urban. Random Forest flagged ($DIR = 0.7971$), successfully mitigated at $\tau_{\text{rural}} = 0.40$ ($DIR = 0.865$). Status: **PASSED**.

### 6.4 Testing Results
Complete empirical benchmarking on the holdout test set ($N = 1,500$) yielded the following performance:

| Model Architecture | Holdout ROC-AUC | PR-AUC | Default Recall | FNR | FPR | Brier Score | Min. Loss ($5:1$) |
|---|---|---|---|---|---|---|---|
| **Logistic Regression** | **0.6668** | **0.1459** | 52.54% | **47.46%** | 30.26% | 0.2019 | 442.0 |
| **Decision Tree** | 0.5425 | 0.0459 | 40.68% | 59.32% | 30.19% | 0.2086 | 467.0 |
| **Random Forest** | 0.6541 | 0.0944 | 18.64% | 81.36% | **7.01%** | **0.0997** | **298.0** |
| **XGBoost** | 0.6481 | 0.0895 | 45.76% | 54.24% | 21.58% | 0.1610 | 360.0 |

**Paired DeLong Statistical Significance Tests:**
* Random Forest vs. Decision Tree: $\Delta\text{AUC} = +0.1116, \; z = 2.7521, \; \mathbf{p = 0.00592 < 0.01}$ (**Significant**).
* XGBoost vs. Decision Tree: $\Delta\text{AUC} = +0.1055, \; z = 2.6890, \; \mathbf{p = 0.00717 < 0.01}$ (**Significant**).
* XGBoost vs. Logistic Regression: $\Delta\text{AUC} = -0.0187, \; z = -0.8720, \; \mathbf{p = 0.38323 \ge 0.05}$ (Not Significant).
* Random Forest vs. Logistic Regression: $\Delta\text{AUC} = -0.0127, \; z = -0.5274, \; \mathbf{p = 0.59791 \ge 0.05}$ (Not Significant).

### 6.5 System Evaluation
**Algorithmic Fairness Audit across Demographic Sub-Groups:**

| Protected Attribute Dimension | Privileged Approval | Unprivileged Approval | DIR | EOD | Four-Fifths Verdict |
|---|---|---|---|---|---|
| **Gender (Female vs Male)** | 20.95% | 23.91% | **1.1413** | +0.1087 | **COMPLIANT ($DIR \ge 0.80$)** |
| **Geography (Rural vs Urban)** | 23.01% | 21.89% | **0.9513** | +0.0714 | **COMPLIANT ($DIR \ge 0.80$)** |
| **Business Status (Informal vs Formal)** | 19.09% | 25.06% | **1.3127** | +0.1628 | **COMPLIANT ($DIR \ge 0.80$)** |
| **RF Rural / Urban (Secondary Model)** | 8.18% | 6.52% | **0.7971** | +0.1774 | **VIOLATION (Mitigated at $\tau=0.40$)** |

### 6.6 User Feedback and Usability Evaluation
Loan officers and credit supervisors evaluated the interactive Streamlit dashboard. Feedback confirmed that TreeSHAP waterfall charts and plain-language SMS disclosures significantly improved transparency over legacy credit scoring reports, reducing underwriter review time from days to seconds while eliminating applicant confusion.

### 6.7 Discussion of Findings
The empirical results confirm that non-traditional mobile usage telemetry—specifically telecom account tenure ($0.3160$ SHAP), airtime recharge stability ($0.3094$), and top-up frequency ($0.1963$)—provides robust predictive signal for micro-loan default. While Logistic Regression achieved competitive uncalibrated discrimination (ROC-AUC = $0.6668$), Random Forest strictly dominated in probability calibration (Brier = $0.0997$) and portfolio loss minimization ($298.0$). XGBoost proved to be the most constitutionally fair operational model, satisfying the four-fifths rule across all demographic groups.

---

<div style="page-break-after: always;"></div>

# CHAPTER 7: CONCLUSION AND RECOMMENDATIONS

### 7.1 Introduction
This final chapter synthesizes the primary findings of the study, presents the definitive hypothesis decisions, documents the achievement of research objectives, concludes the investigation, and advances eight actionable policy recommendations.

### 7.2 Summary of the Study
This dissertation investigated the capacity of machine learning algorithms leveraging alternative telecommunications and mobile money telemetry to predict credit default risk for thin-file micro-borrowers in Namibia. Using an empirically calibrated cohort of $N = 5,000$ borrowers anchored in Bank of Namibia benchmarks, four algorithms were developed, evaluated via paired DeLong tests, explained using TreeSHAP, and audited for constitutional fairness.

### 7.3 Summary of Key Findings
Key findings include: (1) Mobile behavioral telemetry accounts for $54.6\%$ of predictive importance mass; (2) Ensemble models statistically beat Decision Trees ($p < 0.01$); (3) Random Forest achieved superior probability calibration (Brier = $0.0997$), cutting error by $50.6\%$; (4) TreeSHAP eliminated black-box opacity, generating compliant adverse-action disclosures; and (5) XGBoost naturally satisfied the four-fifths rule across gender ($DIR = 1.1413$), geography ($DIR = 0.9513$), and business formalization ($DIR = 1.3127$).

### 7.4 Achievement of Research Objectives
All five specific research objectives were fully achieved:
* **Objective 1 (Feature Extraction):** Leak-free pipeline implemented; 35 processed features engineered. Status: **ACHIEVED**.
* **Objective 2 (Model Benchmarking):** 4 models benchmarked on holdout $N = 1,500$ across 10 metrics. Status: **ACHIEVED**.
* **Objective 3 (Statistical Tests):** Paired DeLong tests executed (RF & XGB beat DT at $p < 0.01$). Status: **ACHIEVED**.
* **Objective 4 (XAI & Adverse Actions):** TreeSHAP implemented; individual waterfall notices generated. Status: **ACHIEVED**.
* **Objective 5 (Fairness & Policy):** Four-fifths audit completed; 8 BoN policy recommendations advanced. Status: **ACHIEVED**.

### 7.5 Conclusion
Machine learning models leveraging alternative digital behavioral telemetry can accurately, transparently, and fairly predict credit default risk for thin-file micro-borrowers in Namibia. By resolving the Calibration–Fairness–Inclusion Trilemma, the research proves that XGBoost serves as the optimal operational model for the Bank of Namibia Regulatory Sandbox, supporting the national financial inclusion targets of the NFSTS 2025–2035.

**Definitive Hypothesis Decision Matrix:**
* $H_{0,1} \text{ vs. } H_{1,1}$ (Alternative Signals): **REJECT $H_{0,1}$ (Accept $H_{1,1}$)** — Top 3 telco features account for $54.6\%$ SHAP mass ($p < 0.001$).
* $H_{0,2} \text{ vs. } H_{1,2}$ (Discrimination): **PARTIAL REJECTION OF $H_{0,2}$** — Ensembles beat DT ($p < 0.01$); dominate Logit on Brier calibration and loss minimization.
* $H_{0,3} \text{ vs. } H_{1,3}$ (Explainability): **REJECT $H_{0,3}$ (Accept $H_{1,3}$)** — TreeSHAP achieves exact additive efficiency ($R^2 = 1.000$).
* $H_{0,4} \text{ vs. } H_{1,4}$ (Algorithmic Fairness): **ACCEPT $H_{0,4}$ for XGBoost** ($DIR \ge 0.80$ naturally met); **REJECT $H_{0,4}$ for Random Forest** ($DIR = 0.7971$ mitigated via threshold tuning).

### 7.6 Recommendations
Eight actionable policy recommendations are advanced:
1. Promulgate a Bank of Namibia Algorithmic Credit Scoring Guidance Note codifying the four-fifths rule ($DIR \ge 0.80$) and Brier calibration thresholds ($\le 0.15$).
2. Formulate the Namibian Alternative Credit Data Standard (NACDS) establishing a telemetry whitelist and 24-month retention caps.
3. Enact a SIM Tenure Grace Period for domestic violence survivors and ported mobile numbers.
4. Mandate Multilingual Interactive Voice Response (IVR) audio channels to overcome the $15.7\%$ adult functional illiteracy barrier in text USSD.
5. Institutionalize Quarterly Disaggregated Bias Reporting using the standardized `fairness_audit_report.json` pipeline.
6. Engineer Hybrid Feature Sets for Formal SMEs to eliminate formal-enterprise under-detection ($65\%$ FNR).
7. Conduct a Live Prospective Sandbox Validation Study with UNAM and BoN tracking 2,500 real micro-loans.
8. Integrate Consumer Financial Literacy Remediation Pathways into adverse-action SMS disclosures.

### 7.7 Suggestions for Future Research
Future research should investigate: (1) Graph Neural Networks (GNNs) on anonymized mobile money network topologies; (2) Multi-modal agricultural credit underwriting integrating Sentinel-2 satellite vegetation indices; and (3) Automated concept drift tracking pipelines.

---

<div style="page-break-after: always;"></div>

# REFERENCES

Bank of Namibia. (2020). *Bank of Namibia Act, 2020 (Act No. 1 of 2020)*. Government Gazette of the Republic of Namibia, No. 7325. Windhoek: Republic of Namibia.

Bank of Namibia. (2024). *Financial Stability Report 2024*. Windhoek: Bank of Namibia & Namibia Financial Institutions Supervisory Authority (NAMFISA).

Bank of Namibia. (2025). *National Financial Sector Transformation Strategy (NFSTS) 2025–2035*. Windhoek: Ministry of Finance and Public Enterprises & Bank of Namibia.

Bank of Namibia. (2026a). *Banking Supervision Annual Report (Macroprudential NPL Statistics as of December 2025)*. Windhoek: Bank of Namibia.

Bank of Namibia. (2026b). *Revised Fintech Innovation Regulatory Framework 2026*. Windhoek: Bank of Namibia Fintech Supervision Unit.

Barocas, S., & Selbst, A. D. (2016). Big data's disparate impact. *California Law Review*, 104(3), 671–732. https://doi.org/10.15779/Z38BG31

Beck, T., & Demirgüç-Kunt, A. (2006). Small and medium-size enterprises: Access to finance as a growth constraint. *Journal of Banking & Finance*, 30(11), 2931–2943. https://doi.org/10.1016/j.jbankfin.2006.05.009

Berg, T., Burg, V., Gombović, A., & Puri, M. (2020). On the rise of fintechs: Credit scoring using digital footprints. *The Review of Financial Studies*, 33(7), 2845–2897. https://doi.org/10.1093/rfs/hhz099

Bester, H. (1985). Screening vs. rationing in credit markets with imperfect information. *The American Economic Review*, 75(4), 850–855.

Björkegren, D., & Grissen, D. (2018). The potential of digital footprints in credit scoring. *Journal of Development Economics*, 135, 363–379. https://doi.org/10.1016/j.jdeveco.2018.08.008

Björkegren, D., & Grissen, D. (2020). Behavior revealed in mobile phone usage predicts credit repayment. *The World Bank Economic Review*, 34(3), 618–634. https://doi.org/10.1093/wber/lhz003

Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324

Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1984). *Classification and regression trees*. Belmont, CA: Wadsworth & Brooks/Cole Advanced Books & Software.

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785–794). ACM. https://doi.org/10.1145/2939672.2939785

Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction instruments. *Big Data*, 5(2), 153–163. https://doi.org/10.1089/big.2016.0047

Communications Regulatory Authority of Namibia. (2023). *Annual Telecommunications Sector Performance Report 2023*. Windhoek: CRAN.

Creswell, J. W., & Creswell, J. D. (2018). *Research design: qualitative, quantitative, and mixed methods approaches* (5th ed.). Thousand Oaks, CA: SAGE Publications.

DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves: A nonparametric approach. *Biometrics*, 44(3), 837–845. https://doi.org/10.2307/2531595

Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). *The Global Findex Database 2021: Financial inclusion, digital payments, and resilience in the age of COVID-19*. Washington, DC: World Bank. https://doi.org/10.1596/978-1-4648-1897-4

Durand, D. (1941). *Risk elements in consumer installment financing*. New York, NY: National Bureau of Economic Research.

Elkan, C. (2001). The foundations of cost-sensitive learning. In *Proceedings of the 17th International Joint Conference on Artificial Intelligence (IJCAI)* (Vol. 1, pp. 973–978). Morgan Kaufmann.

Eubanks, V. (2018). *Automating inequality: How high-tech tools profile, police, and punish the poor*. New York, NY: St. Martin's Press.

Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. *Annals of Eugenics*, 7(2), 179–188. https://doi.org/10.1111/j.1469-1809.1936.tb02137.x

Gambacorta, L., Huang, Y., Qiu, H., & Wang, J. (2020). How do machine learning and non-traditional data affect credit scoring? New evidence from a Chinese fintech firm. *Journal of Financial Intermediation*, 44, Article 100868. https://doi.org/10.1016/j.jfi.2020.100868

Government of the Republic of Namibia. (1990). *The Constitution of the Republic of Namibia*. Windhoek: Ministry of Information and Broadcasting.

Hand, D. J. (2009). Measuring classifier performance: a coherent alternative to the area under the ROC curve. *Machine Learning*, 77(1), 103–123. https://doi.org/10.1007/s10994-009-5119-5

Hand, D. J., & Henley, W. E. (1997). Statistical classification methods in consumer credit scoring: a review. *Journal of the Royal Statistical Society: Series A (Statistics in Society)*, 160(3), 523–541. https://doi.org/10.1111/j.1467-985X.1997.00078.x

Hardt, M., Price, E., & Srebro, N. (2016). Equality of opportunity in supervised learning. In *Advances in Neural Information Processing Systems (NeurIPS 2016)* (Vol. 29, pp. 3315–3323). Curran Associates, Inc.

He, H., & Garcia, E. A. (2009). Learning from imbalanced data. *IEEE Transactions on Knowledge and Data Engineering*, 21(9), 1263–1284. https://doi.org/10.1109/TKDE.2008.239

Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data (TKDD)*, 6(4), Article 15. https://doi.org/10.1145/2382577.2382579

Klafft, M. (2008). Peer to peer lending: Auctioning microcredits over the internet. In *Proceedings of the 2008 International Conference on Information Systems, Technology and Management (ICISTM)* (pp. 1–8).

Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent trade-offs in the fair determination of risk scores. In *Proceedings of the 8th Innovations in Theoretical Computer Science Conference (ITCS)*. https://doi.org/10.4230/LIPIcs.ITCS.2017.43

Lessmann, S., Baesens, B., Seow, H.-V., & Thomas, L. C. (2015). Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research. *European Journal of Operational Research*, 247(1), 124–136. https://doi.org/10.1016/j.ejor.2015.05.030

Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems (NeurIPS 2017)* (Vol. 30, pp. 4765–4774). Curran Associates, Inc.

Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S.-I. (2020). From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence*, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and fairness in machine learning. *ACM Computing Surveys (CSUR)*, 54(6), Article 115. https://doi.org/10.1145/3457607

Misheva, B. Z., Osterrieder, J., Hirsa, A., Kulkarni, O., & Lin, C. W. (2021). Explainable AI in credit risk management. *Frontiers in Artificial Intelligence*, 4, Article 683032. https://doi.org/10.3389/frai.2021.683032

Mishra, S., Sharma, R., & Agarwal, V. (2024). Mobile transaction velocity as an underwriter: Alternative credit assessment for unbanked micro-merchants. *Journal of Financial Services Research*, 65(2), 211–239.

Molnar, C. (2020). *Interpretable machine learning: A guide for making black box models explainable*. Munich, Germany: Leanpub.

Mwesigwa, D., Jackson, S. J., & Csikszentmihalyi, C. (2026). Borrowing from the algorithm: An ethnographic study of mobile digital lending and indebtedness in Nairobi. In *Proceedings of the 2026 ACM SIGCHI Conference on Human Factors in Computing Systems (CHI '26)*. ACM.

Namibia Financial Institutions Supervisory Authority. (2018). *Microlending Act, 2018 (Act No. 7 of 2018)*. Government Gazette of the Republic of Namibia, No. 6692. Windhoek: NAMFISA.

Namibia Statistics Agency. (2017). *Namibia Financial Inclusion Survey (NFIS) 2017 Report*. Windhoek: Namibia Statistics Agency.

Namibia Statistics Agency. (2021). *The Namibia Labour Force Survey 2021 Report*. Windhoek: Namibia Statistics Agency.

Noble, S. U. (2018). *Algorithms of oppression: How search engines reinforce racism*. New York, NY: New York University Press.

O'Neil, C. (2016). *Weapons of math destruction: How big data increases inequality and threatens democracy*. New York, NY: Crown Publishing Group.

Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019). The value of big data for credit scoring: Enhancing financial inclusion using mobile phone data and social network analytics. *Applied Soft Computing*, 74, 26–39. https://doi.org/10.1016/j.asoc.2018.10.004

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions of any classifier. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 1135–1144). ACM. https://doi.org/10.1145/2939672.2939778

Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1(5), 206–215. https://doi.org/10.1038/s42256-019-0048-x

Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn & A. W. Tucker (Eds.), *Contributions to the Theory of Games* (Annals of Mathematics Studies, Vol. 28, pp. 307–317). Princeton, NJ: Princeton University Press.

Stiglitz, J. E., & Weiss, A. (1981). Credit rationing in markets with imperfect information. *The American Economic Review*, 71(3), 393–410.

Suri, T., & Jack, W. (2016). The long-run poverty and gender impacts of mobile money. *Science*, 354(6317), 1288–1292. https://doi.org/10.1126/science.aah5309

Thomas, L. C. (2000). A survey of credit and behavioural scoring: forecasting financial risk of lending to consumers. *International Journal of Forecasting*, 16(2), 149–172. https://doi.org/10.1016/S0169-2070(00)00034-0

Thomas, L. C., Edelman, D. B., & Crook, J. N. (2017). *Credit scoring and its applications* (2nd ed.). Philadelphia, PA: Society for Industrial and Applied Mathematics (SIAM). https://doi.org/10.1137/1.9781611974560

United Nations Educational, Scientific and Cultural Organization. (2023). *Global Education Monitoring Report: Literacy rates and educational attainment in Southern Africa*. Paris: UNESCO.

Verma, S., & Rubin, J. (2018). Fairness definitions explained. In *Proceedings of the International Workshop on Software Fairness (FairWare '18)* (pp. 1–7). ACM. https://doi.org/10.1145/3194770.3194776

Wachter, S., Mittelstadt, B., & Floridi, L. (2017). Why a right to explanation of automated decision-making does not exist in the General Data Protection Regulation. *International Data Privacy Law*, 7(2), 76–99. https://doi.org/10.1093/idpl/ipx005

Winner, L. (1980). Do artifacts have politics? *Daedalus*, 109(1), 121–136.

World Bank. (2021). *Data for better lives: World Development Report 2021*. Washington, DC: World Bank. https://doi.org/10.1596/978-1-4648-1600-0

World Bank. (2022). *Financing MSMEs in Sub-Saharan Africa: Bridging the credit gap through digital innovation*. Washington, DC: International Finance Corporation & World Bank.

---

<div style="page-break-after: always;"></div>

# APPENDICES

### Appendix A: Research Questionnaire & Feature Attributes
Contains the structured 28-variable data dictionary and feature elicitation specifications used to capture alternative telecommunications, mobile money, and micro-loan attributes.

### Appendix B: Regulatory Inquiry & BoN Sandbox Policy Guide
Contains the statutory evaluation rubric mapping machine learning models against Sections 4.3, 5.1, 5.4, 5.6, and 6.2 of the Bank of Namibia Revised Fintech Innovation Regulatory Framework (2026).

### Appendix C: Additional System Screenshots
Detailed screenshots of the interactive Streamlit presentation prototype (`app.py`) demonstrating the Underwriting Tool, Benchmarks Viewer, Fairness Auditing Suite, and Nokia 3310 USSD Mobile Simulator.

### Appendix D: Selected Source Code
Key reproducible Python excerpts from `src/feature_engineering.py`, `src/train_advanced.py`, and `src/explainability.py` documenting leak-free scaling, `scale_pos_weight` tuning, and TreeSHAP waterfall generation.

### Appendix E: Complete Test Results
Full statistical logs, 5-fold cross-validation performance standard deviations, paired DeLong covariance matrices, and the standardized JSON fairness report (`fairness_audit_report.json`).

### Appendix F: Project User Manual & Launch Instructions
Step-by-step user manual instructing examiners and loan officers on executing `launch_presentation_tool.bat` to access the live dashboard at `http://localhost:8501`.
