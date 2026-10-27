# Stage 15 — Final Thesis Dissertation: Master Manuscript Compilation

**Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia: An Empirical and Socio-Technical Investigation under the Bank of Namibia Fintech Regulatory Framework**

| Dissertation Metadata | Detail |
|---|---|
| **Candidate** | **Percyviarance Minsozi Simasiku** |
| **Student ID Number** | **201061589** |
| **Academic Supervisor** | **Mrs. Johanna Nelulu** |
| **Department / Faculty** | Department of Computer Science, School of Computing, Faculty of Science |
| **Institution** | University of Namibia (UNAM) |
| **Degree Program** | Bachelor of Science in Computer Science (Honours) |
| **Date of Submission** | October 2026 (Official Deadline: 03 November 2026) |
| **Master Manuscript Path** | `C:\Users\201061589\Documents\thesis_credit_risk\thesis\full_thesis_manuscript.md` |
| **Modular Chapters Path** | `C:\Users\201061589\Documents\thesis_credit_risk\thesis\chapters\` |
| **Total Manuscript Size** | **175,937 bytes** (approx. 35,000 words across 8 sections) |

---

## 15.1 Structure of the Completed Dissertation

The dissertation has been drafted and compiled in full accordance with the academic guidelines of the University of Namibia and the Department of Computer Science. It comprises the following modular files and master document:

```
thesis/
├── full_thesis_manuscript.md               <-- Master unified dissertation (176 KB)
└── chapters/
    ├── front_matter.md                     <-- Title, Declaration, Abstract, TOC, Acronyms
    ├── chapter_1_introduction.md           <-- Problem statement, RQs, Hypotheses, Scope
    ├── chapter_2_literature_review.md      <-- Credit history, ML, XAI, Fairness, BoN & NFSTS
    ├── chapter_3_methodology.md            <-- Multi-tier data, governance, pipeline, DeLong
    ├── chapter_4_results_and_evaluation.md <-- Benchmarks, DeLong p-values, TreeSHAP, Audits
    ├── chapter_5_sociotechnical_and_regulatory_analysis.md <-- Trilemma, STS critique, 8 Recs
    ├── chapter_6_conclusions_and_future_work.md <-- Synthesis, hypothesis verdicts, future work
    └── references.md                       <-- Exhaustive APA 7th bibliography
```

---

## 15.2 Summary of Dissertation Chapters

### Front Matter
- **Title Page & Declaration:** Formal legal declaration of original work signed by Percyviarance Minsozi Simasiku.
- **Retention and Supervisor Approval:** Conditions of retention in the UNAM Library and certificate of supervisor approval by Mrs. Johanna Nelulu.
- **Abstract (350 words):** Comprehensive summary covering the thin-file exclusion paradox ($77.3\%$ credit exclusion), the Triangulated Multi-Tier Dataset Strategy ($N = 5,000$, BoN $3.93\%$ default calibration), algorithmic benchmarking, TreeSHAP explainability, four-fifths fairness auditing, and the Calibration–Fairness–Inclusion Trilemma.
- **Navigation:** Complete Table of Contents, List of 18 Tables, List of 15 Figures, and List of 35 Acronyms.

### Chapter 1: Introduction
- **Background & Context:** Economic landscape of Namibia, $34\%$ informal workforce, Vision 2030, and the digital mobile phone revolution ($110\%$ SIM penetration).
- **Problem Statement:** The "thin-file" exclusion paradox—how reliance on legacy credit bureau telemetry and collateral locks out unbanked informal entrepreneurs, driving them to predatory informal lenders (*omashikofolas*).
- **Core Research Questions:** Formulation of the Primary Research Question (PRQ) and five Secondary Research Questions (SRQs 1 to 5).
- **Formal Hypotheses:** Rigorous specification of four testable quantitative hypotheses ($H_{0,1}$ to $H_{0,4}$) paired with evaluation protocols.
- **Significance & Scope:** Theoretical, empirical, regulatory, and socio-economic contributions; micro-loan boundaries ($N\$100 - N\$1,500$, $30$-day tenure) modeled on the Tamba Maris USSD pilot in the Bank of Namibia Regulatory Sandbox.

### Chapter 2: Literature Review and Theoretical Framework
- **Historical Evolution:** From judgmental underwriting ("5 Cs of credit") to FICO scorecards and Logistic Regression.
- **Economic Theory:** Stiglitz & Weiss (1981) asymmetric information, adverse selection, moral hazard, and credit rationing.
- **Alternative Data Telemetry:** Landmark studies (Björkegren & Grissen, 2018; Óskarsdóttir et al., 2019; Berg et al., 2020; Gambacorta et al., 2020) establishing mobile usage and wallet velocity as valid credit proxies.
- **Machine Learning Paradigms:** Supervised learning trade-offs across Logistic Regression, Decision Trees, Random Forest, and XGBoost; handling extreme class imbalance ($3.93\%$ default rate) via `scale_pos_weight = 24.36`.
- **Explainable AI (XAI):** Mathematical formulation of Shapley values and TreeSHAP (Lundberg et al., 2020) for adverse-action disclosures.
- **Algorithmic Fairness:** Disparate treatment vs disparate impact, Barocas & Selbst (2016), the four-fifths rule, Equal Opportunity, and impossibility theorems.
- **Namibian Regulatory Landscape:** Bank of Namibia Act, Banking Institutions Act, Revised Fintech Innovation Regulatory Framework (2026), and NFSTS 2025–2035.

### Chapter 3: Methodology and Research Design
- **Research Design:** Pragmatic mixed-methods sequential explanatory framework.
- **Triangulated Multi-Tier Dataset Strategy (Option 4, scored 59/60):** Tier 1 (real African digital credit benchmarks), Tier 2 (NSA NFIS demographics & BoN $3.93\%$ default calibration), Tier 3 (Tamba Maris USSD micro-loan mechanics).
- **Feature Governance Dictionary:** 28 variables evaluated across 6 dimensions; strict constitutional purging of protected attributes (`gender`, `location_region`, `urban_rural`, `business_registration_status`) from training matrix $X$; ethical exclusion of `dispute_complaints_count`.
- **Leak-Free Data Pipeline:** Deterministic seed (42), winsorization at 1st/99th percentiles, informative missingness flags for utility records, `StandardScaler` fit strictly on training set, stratified 70/30 split (3,500 train / 1,500 holdout test).
- **Benchmarking & Testing Protocols:** 5-fold cross-validation with GridSearchCV; paired DeLong tests on holdout ROC-AUC; asymmetric loss function ($C_{FN}=5, C_{FP}=1$); TreeSHAP polynomial computation; four-fifths fairness audit protocol.

### Chapter 4: Empirical Results, Benchmarking, and Explainability Analysis
- **Empirical Benchmarks:** Complete benchmarking across 4 algorithms on holdout test partition ($N = 1,500$). Logistic Regression achieved ROC-AUC = $0.6668$, but suffered from poor calibration (Brier = $0.2019$) and high false positive rate ($30.26\%$). Random Forest achieved outstanding calibration (**Brier Score = 0.0997**, cutting error by $50.6\%$) and minimized portfolio loss to **298.0** at optimal threshold $p^* = 0.5941$.
- **Statistical Significance (DeLong Tests):** Both ensemble models statistically outperformed Decision Trees ($\Delta\text{AUC} > 0.10, \; p < 0.01$). Differences between ensembles and Logistic Regression on uncalibrated ROC-AUC were not statistically significant ($p > 0.35$).
- **TreeSHAP Attributions:** Top predictors established as `account_age_telecom` ($|\phi| = 0.3160$), `airtime_stability_index` ($0.3094$), and `airtime_recharge_frequency` ($0.1963$), accounting for $54.6\%$ of model importance mass. Local waterfall adverse-action decompositions generated for approved (`NAM-11179`, $p = 0.1200$) and declined (`NAM-11764`, $p = 0.6438$) applicants.
- **Fairness Audit:** XGBoost passed the four-fifths rule across all demographic sub-groups: Gender ($DIR = 1.1413$), Geography ($DIR = 0.9513$), and Enterprise Status ($DIR = 1.3127$). Random Forest breached rural fairness ($DIR = 0.7971$), mitigated via threshold tuning ($\tau_{\text{rural}} = 0.40, DIR = 0.865$). EOD flag on business registration ($EOD = +0.1628$) revealed formal SME under-detection ($65\%$ FNR).

### Chapter 5: Socio-Technical and Regulatory Policy Analysis
- **The Calibration–Fairness–Inclusion Trilemma:** Conceptualization of the fundamental structural trade-off between commercial probability calibration, constitutional non-discrimination, and financial inclusion volume.
- **Socio-Technical Critique:** Deconstructing hidden biases in alternative data—the telecom tenure penalty on domestic violence survivors and rural-urban migrants, the informal economy reverse-discrimination paradox, and the $15.7\%$ adult functional illiteracy barrier of text-based USSD menus.
- **Regulatory Governance Matrix:** Statutory mapping against the Bank of Namibia Fintech Regulatory Framework (2026), documenting compliance across non-discrimination, explainability, model governance, and bias audits.
- **Eight Actionable Policy Recommendations:** BoN Algorithmic Credit Scoring Guidance Note; Namibian Alternative Credit Data Standard (NACDS); SIM tenure grace period; multilingual IVR audio channels; quarterly disaggregated bias reporting; formal SME hybrid feature sets; prospective validation pilot; and financial literacy remediation pathways.

### Chapter 6: Conclusions, Limitations, and Future Work
- **Hypothesis Decisions:** Formal decisions documenting rejection of $H_{0,1}$ ($p < 0.001$), partial rejection of $H_{0,2}$ (ensembles beat DT at $p < 0.01$; dominate Logit on calibration/loss), rejection of $H_{0,3}$ (TreeSHAP exact fidelity), and acceptance of $H_{0,4}$ for XGBoost ($DIR \ge 0.80$).
- **Contributions:** Theoretical formulation of the Trilemma, empirical validation of alternative data in Namibia, and regulatory blueprint for central bank sandbox supervision.
- **Limitations:** Absence of live commercial bank data, cross-sectional 30-day product boundary, exclusion of raw CDR graphs for privacy, and static macroeconomic calibration.
- **Future Directions:** 12-month prospective sandbox validation with live Tamba Maris data; Graph Neural Networks (GNNs) on mobile money transaction graphs; multi-modal agricultural credit scoring using satellite remote sensing (NDVI); and longitudinal concept drift monitoring.

### References
- Complete, exhaustive APA 7th edition bibliography containing over 50 verified academic journal articles, central bank regulatory frameworks, statutes, and national survey reports with complete DOIs and formal citations.

---

## 15.3 Verification and Compilation Metrics

| File | Path | Size | Status |
|---|---|---|---|
| **Master Manuscript** | `thesis/full_thesis_manuscript.md` | **175,937 bytes** | **Compiled & Verified** |
| Front Matter | `thesis/chapters/front_matter.md` | 17,018 bytes | Verified |
| Chapter 1 | `thesis/chapters/chapter_1_introduction.md` | 27,454 bytes | Verified |
| Chapter 2 | `thesis/chapters/chapter_2_literature_review.md` | 32,523 bytes | Verified |
| Chapter 3 | `thesis/chapters/chapter_3_methodology.md` | 28,428 bytes | Verified |
| Chapter 4 | `thesis/chapters/chapter_4_results_and_evaluation.md` | 22,574 bytes | Verified |
| Chapter 5 | `thesis/chapters/chapter_5_sociotechnical_and_regulatory_analysis.md` | 22,134 bytes | Verified |
| Chapter 6 | `thesis/chapters/chapter_6_conclusions_and_future_work.md` | 12,375 bytes | Verified |
| References | `thesis/chapters/references.md` | 11,295 bytes | Verified |

---

*Stage 15 is complete. The full dissertation manuscript is ready for academic defense and final submission.*
