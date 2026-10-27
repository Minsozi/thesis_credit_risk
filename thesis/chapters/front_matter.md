# CREDIT RISK PREDICTION FOR FINANCIAL INCLUSION USING MACHINE LEARNING IN NAMIBIA: AN EMPIRICAL AND SOCIO-TECHNICAL INVESTIGATION UNDER THE BANK OF NAMIBIA FINTECH REGULATORY FRAMEWORK

---

**By**

### PERCYVIARANCE MINSOZI SIMASIKU  
**Student Number: 201061589**

A dissertation submitted in partial fulfillment of the requirements for the degree of  
**BACHELOR OF SCIENCE IN COMPUTER SCIENCE (HONOURS)**  
in the  
**Department of Computer Science**  
**School of Computing**  
**Faculty of Science**  
**University of Namibia (UNAM)**

**Supervisor:** Mrs. Johanna Nelulu  
**Date of Submission:** October 2026  

---

## DECLARATION

I, **Percyviarance Minsozi Simasiku**, hereby declare that this study entitled:

> *"Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia: An Empirical and Socio-Technical Investigation under the Bank of Namibia Fintech Regulatory Framework"*

is my own original work and is a true reflection of my research. It has not been submitted either in whole or in part for any degree, diploma, or other qualification at any other institution of higher learning.

No part of this dissertation may be reproduced, stored in any retrieval system, or transmitted in any form or by any means (e.g., electronic, mechanical, photocopying, recording, or otherwise) without the prior permission of the author or the University of Namibia in that behalf.

I, **Percyviarance Minsozi Simasiku**, grant the University of Namibia the right to reproduce this dissertation in whole or in part, in any manner or format, which the University of Namibia may deem fit, for any person or institution requiring it for study and research; providing that the University of Namibia shall waive this right if the whole thesis has been or is being published in a manner satisfactory to the University.

\
\
....................................................................... \
**Percyviarance Minsozi Simasiku** \
Date: 02 October 2026

---

## RETENTION AND USE OF THESIS

I, **Percyviarance Minsozi Simasiku**, being a candidate for the degree of Bachelor of Science in Computer Science (Honours), accept the requirements of the University of Namibia relating to the retention and use of theses deposited in the University Library. 

In terms of these conditions, I agree that the original copy of my dissertation deposited in the Library will be accessible for purposes of study and research, in accordance with the normal regulations of the University Library regarding the use of such documents.

\
\
....................................................................... \
**Percyviarance Minsozi Simasiku** \
Date: 02 October 2026

---

## CERTIFICATE OF SUPERVISOR APPROVAL

The undersigned certifies that she has read and recommends to the Department of Computer Science for acceptance of a dissertation entitled:

> *"Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia: An Empirical and Socio-Technical Investigation under the Bank of Namibia Fintech Regulatory Framework"*

submitted by **Percyviarance Minsozi Simasiku** (Student ID: 201061589) in partial fulfillment of the requirements for the degree of Bachelor of Science in Computer Science (Honours) at the University of Namibia.

\
\
....................................................................... \
**Mrs. Johanna Nelulu** \
Supervisor \
Department of Computer Science \
Faculty of Science \
University of Namibia \
Date: ..............................................................

---

## DEDICATION

This dissertation is dedicated to my family, whose unwavering support, enduring sacrifices, and encouragement have been my foundation throughout my academic journey at the University of Namibia; and to the hardworking micro-entrepreneurs, informal traders, and rural households of Namibia, whose economic vitality drives our nation forward despite enduring financial exclusion.

---

## ACKNOWLEDGEMENTS

First and foremost, I express my deepest gratitude to Almighty God for providing me with strength, health, wisdom, and perseverance throughout the duration of this research.

I wish to express my profound appreciation and heartfelt gratitude to my academic supervisor, **Mrs. Johanna Nelulu**, Department of Computer Science, University of Namibia. Her invaluable mentorship, rigorous academic critique, insightful guidance, and continuous encouragement shaped the direction and execution of this dissertation. Her insistence on methodological integrity and real-world relevance pushed me to achieve standards beyond my initial expectations.

I extend sincere appreciation to the academic and administrative staff of the Department of Computer Science and the School of Computing at UNAM for providing a stimulating learning environment and foundational knowledge throughout my undergraduate studies.

Special recognition is accorded to the **Bank of Namibia (BoN)** for their public dissemination of the *Revised Fintech Innovation Regulatory Framework (2026)* and macroeconomic banking supervision statistics, and to the **Namibia Statistics Agency (NSA)** for publishing comprehensive financial inclusion microdata via the *National Financial Inclusion Survey (NFIS)*. These public resources provided the indispensable empirical anchors for this study.

Finally, I am profoundly indebted to my parents, siblings, and friends for their boundless patience, emotional sustenance, and faith in my abilities during long hours of research, programming, and writing.

---

## ABSTRACT

In Namibia, over $40\%$ of the adult population remains excluded from formal credit markets due to a lack of legacy banking histories, collateral, and formalized financial documentation—a condition known as the "thin-file" exclusion paradox. Traditional linear credit scorecards rely strictly on historical credit bureau telemetry, systematically locking out unbanked informal entrepreneurs, rural smallholders, and youth. 

This dissertation investigates the extent to which machine learning algorithms leveraging non-traditional mobile transactional and behavioral data (e.g., airtime recharge regularity, mobile wallet velocity, and telecom account tenure) can predict credit default risk accurately, transparently, and fairly for thin-file borrowers, while complying with the *Bank of Namibia (BoN) Revised Fintech Innovation Regulatory Framework (2026)* and the *National Financial Sector Transformation Strategy (NFSTS 2025–2035)*.

Adopting an academically defensible **Triangulated Multi-Tier Dataset Strategy**, an empirical cohort of $N = 5,000$ micro-borrowers was generated and conditioned on authentic African digital credit behavioral distributions, calibrated to the Bank of Namibia December 2025 Non-Performing Loan benchmark of $3.93\%$, and constrained to the micro-loan mechanics ($N\$100 - N\$1,500$, $30$-day tenure) of the BoN Sandbox pilot. Four predictive algorithms—Logistic Regression, Decision Trees, Random Forest, and Extreme Gradient Boosting (XGBoost)—were engineered, cross-validated, benchmarked via paired DeLong statistical tests, explained using TreeSHAP, and audited for algorithmic bias across constitutional protected attributes (gender, urban/rural geography, and business formalization).

Empirical findings reveal that alternative behavioral indicators provide statistically significant discriminatory signal ($p < 0.001$), with mobile telecom tenure, airtime recharge stability, and recharge frequency accounting for $54.6\%$ of the total predictive importance mass. While non-linear ensemble models did not statistically outperform regularized Logistic Regression on holdout ROC-AUC alone ($0.65 - 0.67$, $p > 0.35$), both Random Forest and XGBoost statistically outperformed Decision Trees ($\Delta\text{ROC-AUC} > 0.10, \; p < 0.01$). Crucially, under operational banking criteria, Random Forest achieved superior probability calibration (**Brier Score = 0.0997**, cutting error by $50.6\%$ relative to Logistic Regression) and minimized total portfolio default loss to $298.0$ under asymmetric cost penalties ($C_{FN}=5, C_{FP}=1$). 

TreeSHAP local attributions successfully eliminated the "black-box" dilemma, generating compliant individual adverse-action explanation notices that satisfy BoN Framework Section 5.1. The algorithmic fairness audit proved that XGBoost naturally satisfies the international four-fifths rule ($DIR \ge 0.80$) across gender ($DIR = 1.1413$), geographic location ($DIR = 0.9513$), and business registration ($DIR = 1.3127$) without post-hoc distortion. Conversely, Random Forest exhibited disparate impact against rural borrowers ($DIR = 0.7971$), which was successfully mitigated via threshold post-processing ($\tau_{\text{rural}} = 0.40$).

The study articulates the **Calibration–Fairness–Inclusion Trilemma**, demonstrating that pure commercial calibration restricts credit access, whereas national development imperatives mandate prioritizing fairness and inclusion. Eight actionable policy recommendations are advanced to govern digital credit deployment in Namibia.

**Keywords:** Credit Risk Prediction, Financial Inclusion, Machine Learning, Alternative Data, Explainable AI (TreeSHAP), Algorithmic Fairness, Bank of Namibia Fintech Regulatory Sandbox, Namibia.

---

## TABLE OF CONTENTS

- **Declaration**
- **Retention and Use of Thesis**
- **Certificate of Supervisor Approval**
- **Dedication**
- **Acknowledgements**
- **Abstract**
- **Table of Contents**
- **List of Tables**
- **List of Figures**
- **List of Acronyms**
- **Chapter 1: Introduction**
  - 1.1 Background and Context of the Study
  - 1.2 Problem Statement: The Thin-File Exclusion Paradox
  - 1.3 Research Questions and Hypotheses
  - 1.4 Research Objectives
  - 1.5 Significance of the Study
  - 1.6 Delimitations and Scope of the Study
  - 1.7 Organization and Structure of the Dissertation
- **Chapter 2: Literature Review and Theoretical Framework**
  - 2.1 The Evolution of Credit Scoring: From Judgmental Rules to AI
  - 2.2 Financial Exclusion and the Thin-File Dilemma in Sub-Saharan Africa
  - 2.3 Alternative Data and Behavioral Telemetry in Credit Risk
  - 2.4 Machine Learning Algorithms in Credit Decisioning
  - 2.5 Explainable Artificial Intelligence (XAI) in Regulated Lending
  - 2.6 Algorithmic Fairness and Constitutional Equity in Credit Markets
  - 2.7 The Namibian Regulatory Environment: BoN Framework & NFSTS
  - 2.8 Identified Literature Gaps and Conceptual Framework
- **Chapter 3: Methodology and Research Design**
  - 3.1 Research Philosophy and Methodological Framework
  - 3.2 The Triangulated Multi-Tier Dataset Strategy
  - 3.3 Data Governance, Ethical Exclusions, and Feature Dictionary
  - 3.4 Data Pipeline Engineering, Cleaning, and Leakage Prevention
  - 3.5 Model Architectures and Hyperparameter Tuning
  - 3.6 Evaluation Framework and Statistical Hypothesis Testing Protocol
  - 3.7 Explainability (TreeSHAP) and Bias Auditing Architecture
- **Chapter 4: Empirical Results, Benchmarking, and Explainability Analysis**
  - 4.1 Exploratory Data Profiling and Cohort Demographics
  - 4.2 Comparative Algorithmic Benchmarking
  - 4.3 Paired DeLong Tests and Statistical Significance Analysis
  - 4.4 Probability Calibration and Reliability Curves
  - 4.5 Cost-Sensitive Risk Optimization and Asymmetric Loss Minimization
  - 4.6 TreeSHAP Feature Attribution: Global Patterns and Interaction Effects
  - 4.7 Granular Adverse-Action Reason Codes and Case Demonstrations
  - 4.8 Algorithmic Fairness and Responsible AI Audit
- **Chapter 5: Socio-Technical and Regulatory Policy Analysis**
  - 5.1 The Calibration–Fairness–Inclusion Trilemma
  - 5.2 Socio-Technical Critique of Alternative Data in the Namibian Context
  - 5.3 Regulatory Alignment with the Bank of Namibia Fintech Framework (2026)
  - 5.4 Strategic Integration with NFSTS 2025–2035 Objectives
  - 5.5 Actionable Governance Recommendations for Sandbox Deployment
- **Chapter 6: Conclusions, Limitations, and Future Work**
  - 6.1 Summary of Main Findings
  - 6.2 Formal Hypothesis Decisions
  - 6.3 Theoretical, Empirical, and Policy Contributions
  - 6.4 Methodological Limitations
  - 6.5 Future Research Directions and Prospective Validation Roadmap
- **References**

---

## LIST OF TABLES

| Table Number | Caption |
|---|---|
| Table 1.1 | Alignment Matrix: Objectives, Research Questions, and Hypotheses |
| Table 2.1 | Summary of Key Literature Themes on Alternative Data Credit Scoring |
| Table 2.2 | Comparative Summary of Supervised Learning Algorithms in Credit Risk |
| Table 3.1 | Evaluated Dataset Architectural Options Matrix |
| Table 3.2 | Core Feature Dictionary: Categories, Definitions, and Inclusion Rationale |
| Table 3.3 | Winsorization Thresholds and Imputation Strategy for Processed Features |
| Table 3.4 | Hyperparameter Search Grids for Baseline and Ensemble Models |
| Table 4.1 | Demographic and Financial Profile of the Processed Cohort ($N = 5,000$) |
| Table 4.2 | Model Comparison Benchmark Across All Evaluated Metrics (Holdout $N = 1,500$) |
| Table 4.3 | Paired DeLong Statistical Significance Tests on Holdout ROC-AUC |
| Table 4.4 | Cost-Sensitive Threshold Optimization under Asymmetric Loss ($C_{FN}=5, C_{FP}=1$) |
| Table 4.5 | Top 15 Predictors Ranked by Global Mean Absolute TreeSHAP Value ($|\phi|$) |
| Table 4.6 | Local Adverse-Action Decomposition for Applicant `NAM-11764` (Declined) |
| Table 4.7 | Algorithmic Fairness Audit: Demographic Parity, DIR, and EOD Across Protected Groups |
| Table 5.1 | Trade-offs in the Calibration–Fairness–Inclusion Trilemma |
| Table 5.2 | Regulatory Compliance Matrix Against BoN Fintech Framework (2026) |
| Table 6.1 | Comprehensive Hypothesis Testing Decision Matrix |

---

## LIST OF FIGURES

| Figure Number | Caption |
|---|---|
| Figure 1.1 | Conceptual Architecture of the Research Study |
| Figure 3.1 | Triangulated Multi-Tier Dataset Architecture Pipeline |
| Figure 3.2 | End-to-End Machine Learning and Fairness Auditing Workflow |
| Figure 4.1 | Receiver Operating Characteristic (ROC) Curves Across Evaluated Models |
| Figure 4.2 | Precision-Recall (PR) Curves Under Extreme Class Imbalance ($3.93\%$) |
| Figure 4.3 | Probability Calibration Curves (Reliability Diagrams) |
| Figure 4.4 | Portfolio Financial Cost Curves as a Function of Classification Threshold |
| Figure 4.5 | TreeSHAP Global Feature Importance Bar Chart |
| Figure 4.6 | TreeSHAP Summary Beeswarm Plot Showing Directional Risk Impact |
| Figure 4.7 | Four-Panel Partial Dependence Plots for Dominant Non-Linear Features |
| Figure 4.8 | Local Adverse-Action Waterfall Plot for Declined Applicant `NAM-11764` |
| Figure 4.9 | Credit Approval Rates Disaggregated by Model and Protected Demographic Sub-Group |
| Figure 4.10 | Disparate Impact Ratio (DIR) Comparison with the 80% Four-Fifths Reference Line |
| Figure 4.11 | False Negative Rate (FNR) Disparity Analysis Across Protected Sub-Groups |
| Figure 4.12 | Fairness-Accuracy Pareto Frontier for Rural Threshold Mitigation (Random Forest) |
| Figure 5.1 | The Calibration–Fairness–Inclusion Trilemma Diagram |

---

## LIST OF ACRONYMS

| Acronym | Definition |
|---|---|
| **ADCAI** | Alternative Data Credit Artificial Intelligence |
| **AI** | Artificial Intelligence |
| **AUC** | Area Under the Curve |
| **BoN** | Bank of Namibia |
| **CDR** | Call Detail Record |
| **CMA** | Common Monetary Area |
| **CV** | Cross-Validation |
| **DIR** | Disparate Impact Ratio |
| **DPD** | Demographic Parity Difference |
| **EOD** | Equal Opportunity Difference |
| **FN** | False Negative |
| **FNR** | False Negative Rate |
| **FP** | False Positive |
| **FPR** | False Positive Rate |
| **FSCA** | Financial Sector Conduct Authority (South Africa) |
| **IV** | Information Value |
| **IVR** | Interactive Voice Response |
| **LIME** | Local Interpretable Model-agnostic Explanations |
| **ML** | Machine Learning |
| **MNO** | Mobile Network Operator |
| **NAMFISA** | Namibia Financial Institutions Supervisory Authority |
| **NFIS** | National Financial Inclusion Survey |
| **NFSTS** | National Financial Sector Transformation Strategy (2025–2035) |
| **NPL** | Non-Performing Loan |
| **NSA** | Namibia Statistics Agency |
| **OHE** | One-Hot Encoding |
| **PD** | Probability of Default |
| **PR-AUC** | Precision-Recall Area Under the Curve |
| **PRQ** | Primary Research Question |
| **RF** | Random Forest |
| **ROC** | Receiver Operating Characteristic |
| **SHAP** | SHapley Additive exPlanations |
| **SIM** | Subscriber Identity Module |
| **SME** | Small and Medium Enterprise |
| **SRQ** | Secondary Research Question |
| **STS** | Science and Technology Studies |
| **TN** | True Negative |
| **TP** | True Positive |
| **TPR** | True Positive Rate |
| **UNAM** | University of Namibia |
| **USSD** | Unstructured Supplementary Service Data |
| **WoE** | Weight of Evidence |
| **XAI** | Explainable Artificial Intelligence |
| **XGBoost** | Extreme Gradient Boosting |
