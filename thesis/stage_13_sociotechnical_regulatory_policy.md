# Stage 13 — Socio-Technical & Regulatory Policy Analysis

**Credit Risk Scoring for Namibian Digital Micro-Lending: Policy, Society, and Algorithmic Governance**

| Field | Detail |
|---|---|
| Candidate | Percyviarance Minsozi Simasiku (201061589) |
| Supervisor | Mrs. Johanna Nelulu, Dept Computer Science, UNAM |
| Stage | 13 of 15 |
| Date | 20 September 2026 |
| Methodology | In-depth socio-technical and regulatory policy analysis |
| Primary Documents | BoN Fintech Regulatory Framework (2026); NFSTS 2025–2035; NSA NFIS 2017; Namibia Constitution 1990 |

---

## 13.1 Introduction and Analytical Framework

This stage departs from quantitative modelling to conduct an in-depth socio-technical and regulatory policy analysis of the credit risk scoring system developed in Stages 7–12. The analysis is motivated by a foundational premise of Science and Technology Studies (STS): **technical artefacts are never neutral**. Automated credit scoring systems embed social values, reproduce structural inequalities, and interact with regulatory environments in ways that pure performance metrics cannot capture (Eubanks, 2018; O'Neil, 2016; Noble, 2018).

The analysis proceeds in five movements:

1. **Regulatory landscape mapping** — examining Namibia's formal fintech governance architecture
2. **Financial inclusion policy analysis** — situating the system within the NFSTS 2025–2035 national strategy
3. **Socio-technical critique** — interrogating how the technical choices made in Stages 6–12 interact with Namibian social realities
4. **Alternative data legitimacy** — evaluating the epistemological and ethical status of mobile money behavioural signals as creditworthiness proxies
5. **Policy recommendations** — actionable governance guidance for BoN sandbox deployment

### Analytical Framework: Winner's Artefact Theory

Langdon Winner's (1980) seminal question — *Do Artefacts Have Politics?* — provides the analytical anchor. Winner argues that technological designs can embody specific forms of authority and social relationships. Applied to algorithmic credit scoring, the question becomes: whose interests does the model serve, whose are subordinated, and what social arrangements does deployment normalise?

This framework is operationalised through three analytical lenses:

| Lens | Key Question | Thesis Application |
|---|---|---|
| **Socio-technical constitution** | What social world does the model assume and reproduce? | Does airtime-based scoring exclude the non-smartphone poor? |
| **Regulatory legitimacy** | Does the system comply with and advance Namibian law? | BoN sandbox alignment, constitutional non-discrimination |
| **Distributional justice** | Who benefits and who bears risk? | Informal sector, rural women, formal SMEs |

---

## 13.2 The Bank of Namibia Fintech Regulatory Framework (2026)

### 13.2.1 Regulatory Architecture

The Bank of Namibia's 2026 Fintech Regulatory Framework represents a landmark shift from reactive supervision toward proactive *regulatory stewardship* of digital financial innovation. Issued under the authority of the Banking Institutions Act (Act 2 of 1998) and the Payment System Management Act (Act 18 of 2003), the Framework establishes a structured pathway for fintech deployment through a three-stage model:

```
Stage 1: Sandbox Testing         → controlled environment, capped portfolio
Stage 2: Restricted Licensing    → limited commercial deployment, enhanced monitoring
Stage 3: Full Licensing          → standard regulatory requirements apply
```

The thesis prototype — modelled on the *Tamba Maris USSD pilot* — operates at **Stage 1 (Sandbox Testing)**, bounded by:

- **Portfolio cap:** N$1,500 maximum per loan
- **Aggregate exposure:** capped at N$500,000 during sandbox phase
- **Reporting cadence:** monthly algorithmic performance reports to BoN
- **Consumer protection covenant:** mandatory adverse action explanations (Stage 11 SHAP outputs satisfy this requirement)

### 13.2.2 Algorithmic Accountability Provisions

The 2026 Framework introduces, for the first time in Namibian financial regulation, explicit **algorithmic accountability** obligations for automated credit decisioning systems. Five key provisions are directly applicable to this thesis:

**Provision 1 — Non-Discrimination Mandate (Section 4.3)**
> *"No automated credit scoring system deployed within the BoN sandbox shall produce systematically disparate credit outcomes on the basis of sex, race, place of origin, or social status as defined under Article 10 of the Namibian Constitution."*

**Assessment:** The Stage 12 fairness audit demonstrates that the XGBoost model satisfies this provision. No four-fifths rule violation was recorded across gender, urban/rural, or business registration status dimensions. The formal-sector FNR disparity (65% vs 48.72%) does not constitute a constitutional violation (formal-sector applicants are not a protected class under Article 10), but warrants monitoring under the Framework's broader equity mandate.

**Provision 2 — Explainability Covenant (Section 5.1)**
> *"Credit applicants who receive adverse automated decisions shall be entitled to a human-intelligible explanation of the primary factors contributing to the denial."*

**Assessment:** The Stage 11 SHAP adverse action reports (e.g., NAM-11764: declined, primary reason `account_age_telecom` contributes +0.3160 log-odds to default risk) directly satisfy this provision. The explanations are expressed in plain-language terms (telecom account tenure, airtime recharge stability) accessible to a USSD-literate applicant without financial literacy prerequisites.

**Provision 3 — Model Governance (Section 5.4)**
> *"Sandbox licensees must document the training data provenance, feature selection rationale, and periodic performance benchmarking of all deployed scoring models."*

**Assessment:** The Triangulated Multi-Tier Dataset Strategy (Stage 5), Data Dictionary (Stage 6), and 28-variable feature governance framework (Stage 6) collectively satisfy this provision. The literature matrix (Stage 3) documents data provenance. Stages 8–10 provide empirical performance benchmarking with statistical significance testing.

**Provision 4 — Bias Audit Requirement (Section 5.6)**
> *"Annual algorithmic bias audits, including disparate impact ratio testing across BoN-designated protected characteristics, shall be submitted to the Fintech Supervision Unit."*

**Assessment:** Stage 12 provides the required baseline bias audit. The `results/fairness_audit_report.json` is formatted for direct submission to the BoN Fintech Supervision Unit. The Framework requires annual recertification — a recommendation for the deployment phase.

**Provision 5 — Human Override (Section 6.2)**
> *"All automated credit decisions must preserve a human review pathway for applicants who dispute an adverse decision."*

**Assessment:** The adverse action explanation system (Stage 11) provides the informational prerequisite for human review. An operational human review workflow is outside the scope of this prototype but is documented as a deployment requirement in Section 13.6.

### 13.2.3 Gaps in the 2026 Framework

Despite its progressive character, the 2026 Framework contains notable lacunae that limit its effectiveness in governing AI-driven credit scoring:

| Gap | Description | Risk |
|---|---|---|
| **Algorithmic auditing standards** | The Framework mandates bias audits but does not specify which fairness metrics (DIR, EOD, DPD) are required or their acceptance thresholds | Inconsistent auditing across sandbox participants; the four-fifths rule threshold (0.80) was adopted from U.S. EEOC guidelines, not BoN-indigenous standards |
| **Third-party data governance** | The Framework does not regulate the use of telco behavioural data (airtime logs, USSD records) as credit inputs, creating a data rights vacuum | Mobile network operators can monetise subscriber data without explicit credit-use consent |
| **Model version control** | No requirements exist for documenting model updates, retraining schedules, or performance degradation thresholds | Concept drift (shifting default rates post-COVID, post-inflation) may silently degrade model fairness without detection |
| **Cross-border data flows** | The Framework is silent on AI models trained on non-Namibian data (as in this thesis's Tier 1 strategy) | Regulatory uncertainty about the legitimacy of models trained on South African or Kenyan transaction data |

**Policy implication:** These gaps represent an opportunity for BoN to strengthen the 2026 Framework through a forthcoming *Algorithmic Credit Scoring Guidance Note*, which this thesis recommends be developed in consultation with NAMFISA, the Namibia Communications Commission, and civil society organisations.

---

## 13.3 National Financial Sector Transformation Strategy (NFSTS) 2025–2035

### 13.3.1 Strategic Architecture

The NFSTS 2025–2035, launched by the Ministry of Finance and Public Enterprises in collaboration with the Bank of Namibia, sets out a ten-year blueprint for transforming Namibia's financial sector into an inclusive, digitally-enabled, and resilient system. The Strategy's headline target:

> **"Increase the proportion of financially included Namibian adults from 80% to 95% by 2035, with specific attention to rural communities, women, and the informal economy."**

The NFSTS is organised around five strategic pillars:

| Pillar | Focus | Relevance to Thesis |
|---|---|---|
| **P1 — Digital Infrastructure** | Mobile money interoperability, USSD expansion, smartphone penetration | Directly enables the alternative data pipeline (Stages 6–7) |
| **P2 — Inclusive Products** | Nano-lending, micro-insurance, digital savings for underbanked | The N$100–N$1,500 sandbox product falls squarely within P2 |
| **P3 — Consumer Protection** | Financial literacy, dispute resolution, algorithmic transparency | Stage 11 SHAP adverse action explanations operationalise P3 |
| **P4 — Regulatory Modernisation** | BoN Fintech Framework, NAMFISA sandbox, data governance law | Contextualises Stage 12 fairness audit obligations |
| **P5 — Data & Analytics Capacity** | National credit bureau, alternative data frameworks, NSA microdata expansion | Addresses the core data gap that Stage 5's triangulation strategy navigates |

### 13.3.2 Financial Inclusion Baseline (NSA NFIS 2017)

The National Financial Inclusion Survey (NFIS) 2017 — the most comprehensive survey of financial access in Namibia — reveals the structural landscape within which this thesis intervenes:

| Indicator | National | Rural | Female | Informal Workers |
|---|---|---|---|---|
| Formally financially included | 68.4% | 52.1% | 65.7% | 34.2% |
| Mobile money account holders | 41.3% | 29.8% | 38.6% | 27.4% |
| Access to formal credit | 22.7% | 11.3% | 18.9% | 8.6% |
| Credit-excluded but creditworthy* | est. 35–45% | est. 55–65% | est. 40–50% | est. 60–70% |

*Creditworthiness estimate based on BoN NPL 4.3% benchmark applied to excluded population.

This data reveals a **creditworthiness gap**: a substantial proportion of Namibians who are excluded from formal credit are not high-risk borrowers — they are simply invisible to traditional scoring systems that rely on formal employment records, bank statements, and credit bureau histories.

### 13.3.3 The Digital Credit Inclusion Gap

The NFTS 2025–2035 identifies digital credit as the primary instrument for closing the inclusion gap. However, the Strategy acknowledges a *paradox of digital financial inclusion*: the digital infrastructure required to generate the alternative data that enables creditworthiness assessment is itself unevenly distributed.

```
Digital Credit Inclusion Paradox:

  Those MOST excluded from credit          Those MOST included in
  (rural, informal, low-income)            digital infrastructure
                │                                    │
                ▼                                    ▼
         Limited airtime               ──────►  Limited alternative data
         Irregular USSD                         Low SHAP feature values
         Prepaid-only SIM                       High predicted default probability
                │
                ▼
         Further excluded
         by the scoring model
```

This recursive exclusion risk is addressed in this thesis through the **Stage 12 fairness audit**. The finding that rural applicants achieve *higher TPR* (50%) than urban applicants (42.86%) under XGBoost suggests that the model — despite the theoretical paradox — does not empirically reproduce rural exclusion for creditworthy applicants. This is a reassuring but fragile finding: it holds under the current data distribution but must be monitored as the platform scales.

### 13.3.4 Gender and the NFSTS

The NFSTS explicitly targets women's financial inclusion, noting that Namibia's female-headed household rate (38% nationally, 52% in rural areas) creates a distinct financial profile: irregular income, mobile-primary transactions, and high dependency on community savings groups (*mahangu stokvels*).

The Stage 12 finding that the XGBoost model approves female applicants at a *higher rate* (23.91%) than male applicants (20.95%), and detects female creditworthy applicants with *higher sensitivity* (TPR 50% vs 39%), is consistent with the NFSTS objective. However, this result should not be interpreted as structural equality: it reflects the composition of the simulated cohort. Real-world deployment would require gender-stratified performance monitoring aligned with NFSTS Pillar P3 consumer protection obligations.

---

## 13.4 Socio-Technical Critique: What the Numbers Cannot Say

### 13.4.1 The Telecom Tenure Problem

The dominant predictors identified by SHAP analysis (Stage 11) are `account_age_telecom` (SHAP importance 0.316) and `airtime_stability_index` (0.309). These variables encode a specific theory of creditworthiness: **consistent, long-duration mobile engagement signals financial discipline and stability**.

This theory contains a hidden social assumption that warrants critical interrogation:

> **Long telecom account tenure reflects creditworthiness primarily for people who have been digitally mobile for extended periods — a characteristic more common among urban, formally employed, educated adults than among recent rural-to-urban migrants, recently digitised rural communities, or those who have switched SIMs due to domestic violence relocation.**

Three socially specific populations face systematic disadvantage from telecom-centric scoring:

| Population | Mechanism | Magnitude |
|---|---|---|
| **Recent rural-urban migrants** | New SIM on migration; low account age | Account age penalty persists for 6–24 months post-migration |
| **Domestic violence survivors** | SIM replacement for safety reasons; low tenure on new number | False signal of instability; SHAP weight of −0.316 per standard deviation below mean |
| **Elderly non-smartphone adopters** | Recent feature phone adoption; irregular airtime (purchased by family) | Low airtime stability index despite stable household income from pension or remittances |

None of these populations appear explicitly in the Stage 12 protected attribute audit — they are not captured by `gender`, `urban_rural`, or `business_registration_status` categories. This is an **intersectional gap**: the harms fall at the intersection of life circumstance and digital inclusion, not on single demographic axes.

**Recommendation:** BoN sandbox reporting should include disaggregated analysis by *SIM account age quartile* to surface indirect disadvantage for recently-digitised applicants, supplemented by a grace period policy (waiving tenure penalties for accounts 0–6 months old for re-registered numbers).

### 13.4.2 The Informal Economy Paradox

The Stage 12 business registration audit reveals that **informal-sector applicants receive more approvals** (25.06%) than formal-sector applicants (19.09%), and that **formal-sector creditworthy applicants have a dramatically higher FNR** (65.00% vs 48.72%). This counter-intuitive pattern requires socio-technical explanation.

Namibia's informal economy accounts for approximately **34% of employment** (NSA 2021 Labour Force Survey) and is characterised by:
- **High cash transaction frequency** — multiple small M-Pesa/MTC Mobile Money transactions daily
- **Airtime purchase regularity** — small, frequent top-ups rather than large monthly plans
- **Long mobile tenure** — informal workers maintain mobile identities for community network reasons before formalising

These behavioural signatures align precisely with the model's dominant features: high airtime recharge frequency, stable airtime index, long account tenure. Informal workers *look like good credit risks* through the lens of mobile money behaviour, even when their income volatility is higher than formal employees.

Formal-sector workers, by contrast, often:
- Use corporate device plans (airtime paid by employer) — reducing personal airtime recharge frequency signals
- Use banking apps rather than USSD — less USSD transaction data generated
- Have longer but *less frequent* mobile transactions — lower airtime stability index scores

**This is a systematic feature representation failure**: the model's feature set is biased toward informal-sector behavioural signatures. This does not make the model *discriminatory* in a legal sense (informal workers are not a constitutionally protected class), but it creates a **credit mis-allocation risk**: informal workers whose default risk is structurally higher than modelled receive more credit, while formal workers who are genuinely lower-risk are denied.

**Recommendation:** Incorporate formal employment verification signals (even binary: formal/informal employer-verified) and banking transaction count as balancing features in the next model iteration.

### 13.4.3 USSD as Infrastructure and as Exclusion

The Tamba Maris pilot's use of USSD (Unstructured Supplementary Service Data) as the loan application channel is simultaneously the system's greatest strength and its most significant accessibility limitation.

**Strengths of USSD:**
- Functions on basic feature phones without internet connectivity
- Works across all Namibian mobile networks (MTC, TN Mobile, Paratus)
- Operates in areas with 2G-only coverage — approximately 23% of rural Namibia
- Zero-rated in many operator plans — no data cost to applicant
- Session-based: does not require app installation or smartphone literacy

**Limitations of USSD:**
- 182-character session limit requires highly compressed information exchange
- Cannot display documents, images, or complex explanations
- Adverse action explanations (Stage 11 SHAP outputs) cannot be delivered *during* the USSD session — they require a follow-up SMS, which introduces a literacy barrier
- USSD sessions are unencrypted at the air interface — privacy risk for sensitive financial data transmission

**Structural exclusion point:** Applicants who are functionally illiterate — estimated at 15.7% of the Namibian adult population (UNESCO 2023) — cannot navigate USSD menus to self-apply. The system's inclusive intent is constrained by a baseline literacy requirement that systematically excludes the most vulnerable potential beneficiaries.

**Recommendation:** A voice-interface pathway (IVR — Interactive Voice Response) in isiNdonga, Khoekhoegowab, and Afrikaans should be developed as an accessibility complement to the USSD channel, consistent with NFSTS Pillar P1 digital infrastructure inclusivity obligations.

---

## 13.5 Alternative Data Legitimacy: Epistemological and Ethical Analysis

### 13.5.1 The Epistemic Claim

The thesis rests on an epistemic claim: that mobile phone behaviour — telecom account age, airtime recharge patterns, USSD transaction frequency — constitutes *evidence* of creditworthiness. This claim requires careful scrutiny.

The causal chain underpinning this inference is:

```
Mobile Behaviour → Financial Discipline → Repayment Probability
     (proxy)           (latent)              (target)
```

Three conditions must hold for this chain to be epistemically valid:

1. **Correlation:** Mobile behaviour must predict default rates in the training data (validated: AUC 0.65–0.72 across models)
2. **Generalisability:** The correlation must hold beyond the training distribution (partially validated: 5-fold CV AUC ≈ test AUC, suggesting limited overfitting)
3. **Causal plausibility:** There must be a theoretically coherent mechanism linking mobile behaviour to credit risk — not mere statistical coincidence

Condition 3 is the most contested. The literature (Björkegren & Grissen, 2018; Klafft, 2008) suggests several causal mechanisms:

- **Financial discipline hypothesis:** Regular, planned airtime purchases reflect the same executive function and future orientation that predicts loan repayment
- **Social capital hypothesis:** Long mobile tenure reflects stable community embeddedness, which provides informal social collateral reducing default incentive
- **Economic stability hypothesis:** Stable airtime spending implies stable income — irregular, declining airtime often precedes financial distress

These mechanisms are plausible but not proven in the Namibian context. The thesis's use of synthetic data calibrated to Namibian parameters cannot establish causal validity — it can only establish *conditional predictive validity* under the calibration assumptions.

**Academic limitation:** The thesis does not resolve the causal question. It demonstrates that within a carefully constructed synthetic Namibian cohort, mobile behavioural features have predictive validity for credit default. Whether this relationship would hold in a deployed real-world Namibian system requires prospective validation with real-world data — recommended as future work.

### 13.5.2 Ethical Dimensions of Alternative Data Use

The use of behavioural mobile data for credit scoring raises five distinct ethical concerns:

**1. Consent and Data Minimisation**
Namibian mobile subscribers consent to data collection for *telecommunications services*, not for credit scoring. The repurposing of telco data for credit decisions violates the data minimisation principle of the proposed Namibia Data Protection Act (2024 draft). The Tamba Maris pilot must address this through explicit, granular consent at application initiation.

**2. Interpretive Opacity**
Applicants cannot be expected to understand why their airtime recharge *frequency* matters for loan approval. Even with SHAP explanations (Stage 11), the cognitive distance between "you recharge your phone regularly" and "this predicts you will repay your loan" is non-trivial. This creates an informed consent gap even when procedural consent is obtained.

**3. Gaming Risk**
Publication of the model's feature set creates a gaming incentive: applicants may artificially inflate airtime recharge frequency in the weeks before applying. The SHAP dependence plots (Stage 11) show a non-linear relationship between `airtime_recharge_frequency` and SHAP values, which provides partial resistance to manipulation — but sustained gaming over months would defeat this protection.

**4. Poverty Penalty**
The poorest applicants — those with the smallest airtime budgets — will mechanically score lower on `airtime_stability_index` because their spending is more volatile (more subject to income shocks). This means the model may impose a *poverty penalty*: those who need credit most score worst because their precarious finances are reflected in their mobile behaviour. This is structurally distinct from discrimination (it correlates with actual default risk) but is normatively concerning from a financial inclusion perspective.

**5. Feedback Loop Risk**
If the model denies credit to applicants with low airtime stability, those applicants cannot build loan repayment history. Without repayment history, they cannot improve their credit profiles. The denial itself perpetuates the condition that caused it — a textbook *self-fulfilling prophecy* in automated credit systems (Barocas & Moritz, 2016).

---

## 13.6 Policy Recommendations

Drawing on the regulatory analysis (Section 13.2), strategic analysis (Section 13.3), and socio-technical critique (Section 13.4–13.5), this section advances eight policy recommendations for the deployment of alternative-data credit scoring in the Namibian digital micro-lending sector.

---

### Recommendation 1 — Develop a BoN Algorithmic Credit Scoring Guidance Note

**Target:** Bank of Namibia Fintech Supervision Unit  
**Priority:** HIGH — immediate gap in 2026 Framework

The BoN should publish a standalone *Algorithmic Credit Scoring Guidance Note* that specifies:
- Mandatory fairness metrics and their acceptance thresholds (DIR ≥ 0.80 codified as minimum standard)
- Required test set size for fairness auditing (minimum 1,500 records per protected group)
- Approved alternative data categories and their data rights requirements
- Model version control and retraining obligations (annual at minimum)

---

### Recommendation 2 — Establish a Namibian Alternative Credit Data Standard (NACDS)

**Target:** BoN, NAMFISA, Namibia Communications Commission (NCC)  
**Priority:** HIGH — data governance vacuum

A *Namibian Alternative Credit Data Standard* should be developed, establishing:
- A whitelist of approved alternative data categories (mobile money, USSD, utility payments, social grants)
- Mandatory consent architecture for telco-to-lender data sharing
- Data retention limits (24-month rolling window recommended)
- Cross-border data flow rules for models trained on international datasets

---

### Recommendation 3 — Grace Period for Recently-Digitised Applicants

**Target:** Sandbox lenders  
**Priority:** MEDIUM — intersectional fairness gap

Sandbox protocols should mandate a **SIM tenure grace period**: applicants whose current SIM account age is < 6 months but whose historical telco record (via number portability) shows > 24 months of activity should have account age recalculated from portability history. This directly addresses the domestic violence survivor and rural migrant exclusion mechanisms identified in Section 13.4.1.

---

### Recommendation 4 — IVR Accessibility Channel

**Target:** Tamba Maris / sandbox operators  
**Priority:** MEDIUM — USSD literacy barrier

Implement an IVR (Interactive Voice Response) application pathway in the three most widely spoken Namibian languages (Oshiwambo, Khoekhoegowab, Afrikaans), enabling voice-guided loan applications for functionally illiterate applicants. This is consistent with NFSTS Pillar P1 and operationally feasible through NCC-licensed VoIP providers.

---

### Recommendation 5 — Quarterly Disaggregated Monitoring Reports

**Target:** All BoN sandbox participants  
**Priority:** HIGH — regulatory accountability

BoN should require quarterly disaggregated performance reports covering:
- Approval rates by gender, region, and registration status
- FNR by protected group (the credit exclusion metric)
- DIR trends over time (detecting gradual fairness degradation)
- Default rates by protected group (detecting mis-calibration)

The `fairness_audit_report.json` generated in Stage 12 provides a template for this reporting.

---

### Recommendation 6 — Formal Sector Feature Augmentation

**Target:** Tamba Maris / model developers  
**Priority:** MEDIUM — formal SME credit mis-allocation

Integrate formal-sector employment verification signals into the next model iteration:
- Binary employer verification flag (formal/informal, verified via NamRA tax records)
- Bank transaction frequency (even aggregated: >3 bank transactions/month binary flag)
- Formal payroll receipt indicator (salary credit to mobile wallet)

These features would reduce the formal-sector FNR (currently 65% under XGBoost) toward parity with the informal sector without disadvantaging informal workers.

---

### Recommendation 7 — Prospective Validation Study

**Target:** UNAM Department of Computer Science / BoN / Tamba Maris  
**Priority:** HIGH — epistemic limitation of synthetic data

This thesis establishes *conditional predictive validity* in a synthetic Namibian cohort. Before any commercial deployment beyond the sandbox, a **prospective validation study** must be conducted using real loan application and repayment data from the Tamba Maris pilot. The study should:
- Recruit minimum 2,000 applicants over 12 months
- Apply the Stage 7 feature engineering pipeline to real telco data
- Compare predicted default probability (Stage 9 XGBoost PD) to actual 90-day payment outcomes
- Report all fairness metrics from Stage 12 on real observed data

---

### Recommendation 8 — Consumer Financial Literacy Integration

**Target:** BoN Financial Literacy Programme / Tamba Maris  
**Priority:** MEDIUM — informed consent gap

The USSD application interface should include a pre-application disclosure module (2–3 USSD screens) explaining:
- What data is used in the scoring decision
- How applicants can improve their score (increase airtime stability, maintain account)
- How to dispute a denial (human review pathway)

This addresses the interpretive opacity concern (Section 13.5.2) and satisfies the BoN Framework's consumer protection mandate.

---

## 13.7 Situating the Thesis in African Fintech Literature

The thesis's socio-technical findings contribute to a growing body of African fintech scholarship that challenges the uncritical adoption of Northern-hemisphere AI credit scoring frameworks.

### 13.7.1 Contrast with Kenyan M-Shwari Experience

Kenya's M-Shwari (NCBA × Safaricom) represents the closest real-world analogue to the Tamba Maris sandbox model. Launched in 2012, M-Shwari extended micro-credit to over 12 million previously unbanked Kenyans by 2020 using M-Pesa mobile money behaviour as the primary creditworthiness signal.

Key lessons for Namibia:

| M-Shwari Finding | Namibian Implication |
|---|---|
| 90-day CRB blacklisting for N$1,500 defaults destroyed credit access for 3 years | Namibia must adopt proportionate consequences — sandbox loans should not feed the NamCBB blacklist until post-sandbox |
| Feature drift: M-Pesa behaviour changed post-smartphone penetration | Annual model retraining required (Recommendation BoN-4, aligned with Stage 13 Rec. 3) |
| Women outperformed men on repayment but were systematically offered lower credit limits | Namibia's gender TPR parity (Stage 12) should be leveraged to offer equal limit access, not perpetuate asymmetry |
| Digital literacy gap caused accidental loan acceptance through USSD confusion | Namibia's IVR recommendation directly addresses this |

### 13.7.2 West African Contrast: Francophone Regulatory Divergence

West African francophone countries (Senegal, Côte d'Ivoire) operating under BCEAO regulations have taken a more cautious approach, requiring *prior regulatory approval* for each new AI credit scoring feature introduced. While this limits innovation velocity, it creates stronger accountability checkpoints. The BoN 2026 Framework's sandbox-first approach is more permissive — appropriate given Namibia's smaller market — but should be complemented by the Guidance Note recommended in Section 13.6.

### 13.7.3 South African FSCA Comparison

The Financial Sector Conduct Authority (FSCA) of South Africa issued a *Discussion Paper on Artificial Intelligence in Financial Services* (2024), proposing risk-tiered regulation of AI systems with credit decisioning classified as *high-risk*. Namibia, which maintains strong regulatory alignment with South Africa through the Common Monetary Area, should monitor FSCA's forthcoming AI regulation for emerging standards applicable to the Namibian context under NFSTS Pillar P4.

---

## 13.8 Theoretical Contribution: The Calibration–Fairness–Inclusion Trilemma

This thesis's empirical and analytical work surfaces a fundamental trilemma in credit scoring for financial inclusion contexts:

$$\text{Calibration} \quad \xleftrightarrow{\text{tension}} \quad \text{Fairness} \quad \xleftrightarrow{\text{tension}} \quad \text{Inclusion}$$

| Trade-off | Mechanism | Evidence in this Thesis |
|---|---|---|
| **Calibration vs Inclusion** | Perfect calibration (accurate PD estimates) at 4.3% default rate requires a high decision threshold, denying credit to many low-probability defaulters | RF Brier = 0.0997 (excellent calibration) achieved with FNR = 82% (massive credit exclusion) |
| **Fairness vs Inclusion** | Enforcing equal approval rates across groups (demographic parity) may reduce credit to groups with genuinely higher default probability | Formal-sector fairness parity would require increasing formal approvals despite 65% FNR — at the cost of model integrity |
| **Calibration vs Fairness** | Group-specific thresholds can equalise approval rates but introduce within-group miscalibration | RF rural/urban DIR can be restored to 0.85 at τ = 0.40, but with reduced accuracy for the rural group |

This trilemma cannot be dissolved by technical optimisation — it requires *normative* choices about which objectives take priority in the Namibian policy context. This thesis recommends that the BoN explicitly adopt the following priority ordering for sandbox Phase 1:

1. **Constitutional non-discrimination** (DIR ≥ 0.80) — non-negotiable
2. **Credit inclusion** (FNR ≤ 60% for all groups) — primary policy objective
3. **Portfolio calibration** (Brier ≤ 0.15) — commercial viability constraint
4. **Overall accuracy** — secondary metric

This ordering reflects the *developmental state* logic of the NFSTS 2025–2035: financial inclusion is the mission, not profit maximisation.

---

## 13.9 Chapter Summary

Stage 13 has conducted a rigorous in-depth socio-technical and regulatory policy analysis of the credit risk scoring system developed across Stages 7–12. Key findings:

1. **The XGBoost model substantially satisfies BoN Fintech Regulatory Framework 2026 provisions** on non-discrimination, explainability, model governance, and bias auditing. The formal-sector FNR disparity and the USSD literacy barrier are the two primary gaps requiring operational remedy.

2. **The NFSTS 2025–2035 establishes a policy environment that is hospitable but demanding.** Financial inclusion is a national priority; algorithmic credit scoring is positioned as a key instrument. But the Strategy's ambition — 95% financial inclusion by 2035 — requires that scoring models avoid the recursive exclusion paradox.

3. **Telecom-centric alternative data is epistemically plausible but socially partial.** It systematically advantages long-tenured, frequent-transaction informal urban mobile users and may structurally disadvantage recent migrants, domestic violence survivors, elderly adopters, and formal-sector employees whose mobile behaviour doesn't match the model's creditworthiness signatures.

4. **The Calibration–Fairness–Inclusion Trilemma** is an irreducible normative challenge that BoN must resolve through explicit priority-setting, not through technical optimisation alone.

5. **Eight policy recommendations** are advanced for BoN, NAMFISA, sandbox operators, and UNAM, spanning regulatory guidance, data governance, feature augmentation, accessibility, and prospective validation.

---

*Next: Stage 14 — Synthesis of Findings and Hypothesis Conclusions*
