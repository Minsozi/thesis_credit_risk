# Stage 1: Academic Audit of Thesis Proposal & Research Objectives

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Department:** Department of Computer Science, University of Namibia  
**Degree Focus:** Bachelor of Science in Computer Science (Honours) / Data Science  
**Target Completion:** November 3, 2026 (10-Week Academic Cycle)  

---

## 1. Executive Summary

This Stage 1 Audit conducts a rigorous, critical evaluation of the thesis proposal titled:
> **"Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia"**

The evaluation is conducted strictly against the operational constraints, academic standards, and ethical directives set out in the project prompt template. The proposal possesses exceptionally strong conceptual framing, well-grounded economic theory (Stiglitz & Weiss credit rationing), and timely alignment with Namibian fintech and regulatory initiatives (Bank of Namibia Revised Fintech Innovation Regulatory Framework 2026; Tamba Maris pilot).

However, the audit reveals **three critical vulnerabilities** that must be addressed immediately to ensure the thesis is academically defensible, practically executable within the 10-week window, and fully compliant with data ethics:
1. **The "Real Namibian Data" Reality Check:** There is a mismatch between the proposal's claim of calibrating models on "localized Namibian borrower transaction data" and the real-world non-availability of public, loan-level Namibian mobile money or bank default logs.
2. **Qualitative Fieldwork Scope Risk:** Attempting to obtain UNAM IRB clearance, recruit and interview 10–15 commercial bank and regulatory executives, and conduct 3–4 focus group discussions across urban/rural communities within 10 weeks represents an existential delivery risk for an Honours project.
3. **Benchmarking & Metric Gaps:** The proposal omits simple interpretable Decision Trees (mandated as a baseline) and overlooks PR-AUC and model probability calibration (Brier score / calibration curves), which are critical in credit scoring where default events are sparse and risk probabilities dictate loan pricing.

---

## 2. Detailed Section-by-Section Audit

### 2.1 Degree Title & Academic Framing
* **Current Proposal:** Bachelor of Science in Computer Science (Honours).
* **Prompt Template:** BSc Honours Data Science thesis titled: *"Credit Risk Prediction for Financial Inclusion"*.
* **Assessment:** The methodologies proposed (machine learning classification, feature engineering, explainable AI, fairness audits, and econometric modeling of credit risk) fall squarely within Applied Data Science and Computational Finance.
* **Recommendation:** Confirm with your supervisor whether your formal degree registration is B.Sc. Computer Science (Honours) with a Data Science specialisation, or if the thesis title should be formatted uniformly across both UNAM records and the project repository.

---

### 2.2 Research Problem Statement & Namibian Policy Context
* **Strengths:**
  * Accurately characterizes the informal sector in Namibia (contributing **24.7% of GDP** and **57.7% of total employment** based on Bank of Namibia 2026 data).
  * Appropriately incorporates demand-side barriers from the **Namibia Financial Inclusion Survey (NFIS 2017)** (e.g., only 12.8% of adults access bank credit; 57.9% do not borrow; 95.1% cite fear of debt).
  * Explicitly connects theoretical credit rationing (Stiglitz & Weiss, 1981) to the lack of formal credit bureau histories for thin-file borrowers.
* **Identified Policy Gap:**
  * The prompt template explicitly mandates integrating the **Bank of Namibia Financial Sector Transformation Strategy (NFSTS) 2025–2035**, which identifies limited access to credit and financial inclusion as core national strategic challenges.
  * While the proposal cites the *Revised Fintech Innovation Regulatory Framework 2026* and the *SADC Financial Inclusion Strategy 2023–2028*, it does not yet ground itself in the NFSTS 2025–2035.
* **Assumption Scrutiny (Mandated by Template):**
  * The template instructs: *"Do not assume that this statement [informal businesses lack formal records and are poorly represented] is automatically true. Find credible evidence supporting, qualifying or challenging it."*
  * *Critique:* The proposal currently takes this as an axiom. To achieve Honours-level rigor, the literature and methodology must actively discuss **counter-evidence and boundary conditions**:
    1. Some informal businesses maintain internal paper ledgers or informal rotating credit associations (*stokvels* / savings groups) that demonstrate repayment discipline, but which remain uncaptured digitally.
    2. Digital alternative data (such as airtime or mobile wallet logs) can be noisy, volatile, or seasonal, meaning a high transaction frequency does not automatically equate to debt-servicing capacity.
    3. Mobile money adoption in Namibia, while growing, has historical structural differences compared to Kenya (e.g., higher cash preference, differing tariff structures, bank-led wallet models like e-Wallet vs. telco-led M-Pesa).

---

### 2.3 Research Objectives & Algorithmic Scope
The proposal establishes four sub-objectives. Below is the comparative audit against the template directives:

| Proposal Sub-Objective | Current Formulation | Prompt Template Mandate | Recommended Alignment |
| :--- | :--- | :--- | :--- |
| **Objective 1: Model Design** | Implements Logistic Regression, Random Forest, and XGBoost. | Mandates investigating at minimum: **Logistic Regression, Decision Tree, Random Forest, and XGBoost**. | **Add Decision Tree:** A simple decision tree is crucial as an intermediate interpretable baseline between linear scorecards and non-linear ensembles. |
| **Objective 2: Feature Engineering** | Extracts behavioral proxies (mobile money regularity, airtime top-up frequency, utility payments). | Emphasizes feature validity, legal/ethical admissibility, expected missingness, and proxy bias. | **Formalize Data Dictionary & Screening:** Explicitly verify that features do not act as illegal proxies for protected attributes (e.g., geographic location proxies for ethnicity/race). |
| **Objective 3: Benchmarking Metrics** | Evaluates on Accuracy, Precision, Recall, F1-Score, and ROC-AUC. | Mandates: **Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC, Confusion Matrix, Calibration, FPR, and FNR**. Emphasizes **False Negatives**. | **Add PR-AUC & Probability Calibration:** On imbalanced credit datasets (where defaults are typically 4–10%), ROC-AUC can present an overly optimistic picture. PR-AUC is essential. Furthermore, predicted probabilities must be well-calibrated (Brier score / Platt scaling) because lending decisions and expected loss calculations rely on true default probabilities. |
| **Objective 4: XAI, Fairness & Sandbox** | Formulates deployment framework with SHAP, LIME, demographic parity, and BoN Sandbox alignment. | Requires explainability (SHAP, feature importance, individual explanations), group fairness, and responsible AI governance. | **Expand Fairness Metrics:** Demographic parity can force equal acceptance rates regardless of risk, which may harm vulnerable groups by over-indebting them. Include **Equal Opportunity** (equal True Positive / Default Recall across groups) and **Predictive Parity**. |

---

### 2.4 The "Real Data" Paradox & Methodological Feasibility (Critical Issue)

> [!WARNING]
> **Core Empirical Risk: Real Namibian Credit Data is Not Publicly Available.**
> The proposal repeatedly states that the machine learning models will be *"calibrated specifically on localized Namibian borrower transaction data"*. However, granular, transaction-level mobile money logs matched to loan default outcomes are strictly proprietary to institutions like MTC (Maris), Telecom Namibia, commercial banks, or microlenders. Public repositories from the Bank of Namibia or NSA contain only aggregated macro-level time series or survey percentages, not microdata suitable for training machine learning classifiers.

The prompt template establishes strict ethical and academic directives:
* *"Do NOT fabricate research results, participants, interviews, datasets, citations, model performance, financial records or empirical findings."*
* *"Do NOT invent data and present it as real-world Namibian data."*
* *"If real data is unavailable, clearly identify the limitation and propose an academically defensible alternative..."*

#### Academically Defensible Solution (The Triangulated Dataset Strategy):
Rather than risking academic dishonesty or hitting a dead end waiting for non-disclosure agreements, the thesis should adopt the following **3-tier defensible methodology**:
1. **Tier 1: High-Validity Real-World Benchmark Dataset:** Train and benchmark the algorithms (Logistic Regression, Decision Tree, Random Forest, XGBoost) on an established, peer-reviewed, open-access alternative credit / financial inclusion dataset (e.g., South American telecom credit dataset by Björkegren & Grissen, or the World Bank / Kaggle / Zindi African digital lending datasets). This proves the mathematical and algorithmic validity of the framework on real borrower repayment outcomes.
2. **Tier 2: Empirical Namibian Macro & Contextual Conditioning:** Calibrate risk thresholds, baseline default rates (e.g., BoN individual NPL rate of ~4.3%–5.9%), income/turnover bands, and informal sector parameters using verified statistics from the Bank of Namibia Annual Reports, Financial Stability Reports, and the NSA NFIS 2017.
3. **Tier 3: Documented, Parameterized Synthetic Simulation for the BoN Sandbox:** Explicitly construct and document a synthetic simulation environment calibrated to Namibian micro-transaction patterns (airtime recharges in N$, wallet transaction frequencies, utility bills) to demonstrate how the ADCAI pipeline functions within the Bank of Namibia Regulatory Sandbox. Transparently declare every data-generation assumption, ensuring zero misrepresentation.

---

### 2.5 Scope of Qualitative Fieldwork in a 10-Week Academic Cycle

The proposal specifies:
* 10–15 key informant interviews (commercial bank risk heads, Bank of Namibia regulators, fintech developers).
* 3–4 Focus Group Discussions (FGDs) with informal traders and unbanked borrowers across urban and rural locations.
* Audio transcription, NVivo coding, and thematic analysis.

> [!CAUTION]
> **Operational Timeline Bottleneck:**
> In an accelerated 10-week Honours cycle (Aug 19 – Nov 3, 2026), obtaining formal UNAM Institutional Review Board (IRB) ethical clearance, scheduling corporate interviews with bank executives, executing multi-site rural/urban focus groups, transcribing hours of audio, and running NVivo thematic analysis—all while simultaneously coding, training, validating, and explaining four ML models—is an extreme operational risk.

#### Recommended Refinement:
* **Option A (Full Mixed-Methods if Feasible):** If ethical clearance has already been submitted and institutional contacts are pre-arranged, streamline the sample to **5–6 targeted key expert interviews** (e.g., 2 credit risk officers, 1 BoN/regulatory specialist, 2 fintech engineers) and focus groups limited to a single accessible local market hub (e.g., Windhoek informal traders).
* **Option B (Documentary Policy Analysis + Quantitative Core):** If institutional access is delayed, pivot Phase 2 from extensive fieldwork to a **Rigorous Socio-Technical & Regulatory Policy Analysis** (evaluating the BoN Sandbox Framework 2026, NFSTS 2025–2035, and international digital lending case studies), supplemented by an expert consultation questionnaire or pilot interview guide.

---

## 3. Audit of the Conceptual Framework (ADCAI)

The **Alternative Data Credit Assessment and Inclusion (ADCAI)** Framework presented in Section 2.6 of the proposal is conceptually sound and innovative. It links three coherent stages:
1. **Alternative Inputs Ingestion:** Ingesting non-traditional data (airtime, wallet regularity, bill payments) with demographic safeguards.
2. **Ensemble Machine Learning & Fairness Audit:** Model training, multi-metric benchmarking, and subgroup bias checks.
3. **Explainable Output & Regulatory Sandbox Loop:** Translating probabilities into tiered risk categories (Low, Medium, High), attaching SHAP/LIME decision scorecards, and feeding repayment performance back into model recalibration.

**Audit Enhancements for ADCAI:**
* Incorporate an explicit **Data Governance & Consent Gateway** at Stage 1 (addressing data protection, customer consent, and phone data privacy concerns).
* Incorporate **Cutoff Threshold Tuning** at Stage 3: In financial inclusion, the decision threshold between approval and denial should not simply default to $p = 0.5$. It must be calibrated against the lender's cost matrix (cost of false positive vs. cost of false negative) to maximize safe inclusion without triggering default spikes.

---

## 4. Key Recommendations Summary for User Approval

1. **Clarify Degree & Title:** Standardize on "BSc Honours Data Science / Computer Science: Credit Risk Prediction for Financial Inclusion in Namibia".
2. **Expand Benchmark Models:** Formally add **Decision Tree** to Logistic Regression, Random Forest, and XGBoost.
3. **Upgrade Evaluation Metrics:** Formally integrate **PR-AUC, Brier Score / Calibration Curves, False Positive Rate (FPR), and False Negative Rate (FNR)**.
4. **Adopt the Triangulated Dataset Strategy:** Resolve the "real data" paradox by combining a validated international benchmark credit dataset with documented, empirical Namibian contextual parameterization.
5. **Calibrate Fieldwork Scope:** Streamline qualitative fieldwork to protect the 10-week submission deadline while maintaining rigorous academic depth.
6. **Incorporate NFSTS 2025–2035:** Embed the Bank of Namibia Financial Sector Transformation Strategy 2025–2035 into the policy and literature foundations.
