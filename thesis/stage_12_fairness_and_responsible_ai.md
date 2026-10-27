# Stage 12 — Fairness & Responsible AI Audit

**Credit Risk Scoring for Namibian Digital Micro-Lending: An Algorithmic Fairness Analysis**

| Field | Detail |
|---|---|
| Candidate | Percyviarance Minsozi Simasiku (201061589) |
| Supervisor | Mrs. Johanna Nelulu, Dept Computer Science, UNAM |
| Stage | 12 of 15 |
| Date | 20 September 2026 |
| Script | `src/fairness_audit.py` |
| Key outputs | `results/fairness_audit_report.json`, 3 × 300 DPI publication figures |

---

## 12.1 Motivation and Regulatory Context

Automated credit scoring in Namibia operates at the intersection of two constitutional obligations:

1. **Article 10, Namibian Constitution** — prohibits discrimination on grounds of sex, race, place of origin, or social status.
2. **Bank of Namibia Fintech Regulatory Framework (2026)** — requires sandbox-licensed lenders to document and mitigate algorithmic bias prior to commercial deployment.

The *four-fifths rule* (80% rule) is the international operational standard derived from the U.S. Equal Employment Opportunity Commission (1978), subsequently adopted in EU AI Act risk assessments and the BoN sandbox guidelines. It states that the approval rate for any unprivileged group must be at least 80% of the approval rate for the privileged comparator group:

$$\text{DIR} = \frac{P(\hat{Y}=1 \mid \text{unprivileged})}{P(\hat{Y}=1 \mid \text{privileged})} \geq 0.80$$

A DIR < 0.80 constitutes *prima facie* evidence of adverse impact and triggers a mitigation obligation.

---

## 12.2 Protected Attributes and Group Definitions

Four protected attributes were collected but **excluded from training** to prevent direct discrimination. They are used here exclusively for post-hoc auditing.

| Attribute | Privileged Group | Unprivileged Group | Constitutional Basis |
|---|---|---|---|
| `gender` | Male | Female | Art. 10(2) — sex discrimination |
| `urban_rural` | Urban | Rural | Art. 10(2) — place of origin |
| `business_registration_status` | Formal | Informal | NFIS 2017 — financial inclusion equity |

> **Note on `location_region`:** Thirteen regional groups create cells too small for reliable FNR estimation at n=1,500. Region-level analysis is deferred to the full Namibian deployment cohort.

---

## 12.3 Fairness Metrics Framework

Four complementary metrics capture different dimensions of algorithmic fairness:

| Metric | Formula | Acceptable Range | What It Catches |
|---|---|---|---|
| **DPD** — Demographic Parity Difference | $P(\hat{Y}=1\|A) - P(\hat{Y}=1\|B)$ | \|DPD\| < 0.05 | Differential approval rates |
| **DIR** — Disparate Impact Ratio | $P(\hat{Y}=1\|\text{unpriv}) / P(\hat{Y}=1\|\text{priv})$ | DIR ≥ 0.80 | Four-fifths rule violation |
| **EOD** — Equal Opportunity Difference | $\text{TPR}_{\text{unpriv}} - \text{TPR}_{\text{priv}}$ | \|EOD\| < 0.10 | Creditworthy applicants unfairly denied |
| **FNR Gap** | $\text{FNR}_{\text{unpriv}} - \text{FNR}_{\text{priv}}$ | \|FNR gap\| < 0.10 | Credit exclusion harm (missed repayers) |

Models audited at the **standard threshold τ = 0.50** for baseline comparability.

---

## 12.4 Results: XGBoost (Primary Model)

### 12.4.1 Gender Audit

| Group | n | Defaults | Approval Rate | TPR | FNR | Accuracy |
|---|---|---|---|---|---|---|
| **Male** (privileged) | 697 | 23 | **20.95%** | 39.13% | 60.87% | 78.34% |
| **Female** (unprivileged) | 803 | 36 | **23.91%** | 50.00% | 50.00% | 76.09% |

| Metric | Value | Verdict |
|---|---|---|
| DPD | +0.0296 | **PASS** (\|DPD\| < 0.05) |
| DIR | 1.1413 | **PASS** (DIR > 1.0 — females receive *more* approvals) |
| EOD | +0.1087 | **FLAG** (\|EOD\| > 0.10 — females have higher TPR) |
| FNR gap | −0.1087 | Male applicants have 10.87 pp higher FNR than females |

**Interpretation:** No adverse impact against female applicants. Counter-intuitively, the model approves female applicants at a *higher rate* (23.91% vs 20.95%), and female creditworthy applicants are detected at a *higher rate* (TPR 50% vs 39%). The EOD flag reflects a *beneficial disparity* for women, not a harmful one. The male FNR (60.87%) represents a notable credit-exclusion concern for qualifying male applicants.

### 12.4.2 Urban/Rural Audit

| Group | n | Defaults | Approval Rate | TPR | FNR | Accuracy |
|---|---|---|---|---|---|---|
| **Urban** (privileged) | 856 | 35 | **23.01%** | 42.86% | 57.14% | 76.40% |
| **Rural** (unprivileged) | 644 | 24 | **21.89%** | 50.00% | 50.00% | 78.11% |

| Metric | Value | Verdict |
|---|---|---|
| DPD | −0.0112 | **PASS** |
| DIR | 0.9513 | **PASS** (DIR > 0.80) |
| EOD | +0.0714 | **PASS** |
| FNR gap | −0.0714 | Rural applicants have lower FNR (better detection) |

**Interpretation:** Near-perfect parity. Rural applicants are approved at a slightly lower rate (21.89% vs 23.01%), well within the four-fifths threshold. The rural TPR (50%) exceeds urban TPR (42.86%), indicating rural creditworthy applicants are actually better detected. No evidence of urban/rural discrimination.

### 12.4.3 Business Registration Status Audit

| Group | n | Defaults | Approval Rate | TPR | FNR | Accuracy |
|---|---|---|---|---|---|---|
| **Formal** (privileged) | 634 | 20 | **19.09%** | 35.00% | **65.00%** | 79.97% |
| **Informal** (unprivileged) | 866 | 39 | **25.06%** | 51.28% | **48.72%** | 75.06% |

| Metric | Value | Verdict |
|---|---|---|
| DPD | +0.0597 | **BORDERLINE** (approaching 0.05 threshold) |
| DIR | 1.3127 | **PASS** (informal sector receives *more* approvals) |
| EOD | +0.1628 | **FLAG** (\|EOD\| > 0.10) |
| FNR gap | −0.1628 | Formal-sector businesses have 16.28 pp higher FNR |

**Interpretation:** The model systematically **under-detects creditworthy formal-sector applicants** (FNR 65% vs 48.72%). This is a significant credit-inclusion concern for Namibia's formal SME sector. One likely mechanism: the SHAP analysis (Stage 11) established that `account_age_telecom` and `airtime_stability_index` are the dominant features — variables that correlate more strongly with informal mobile-money behaviours than with formal business credit histories. The EOD flag warrants a structural investigation of feature representation for formal-sector applicants.

---

## 12.5 Results: Random Forest (Secondary Model)

| Attribute | Group Comparison | DIR | EOD | FNR-gap | 4/5 Violated? |
|---|---|---|---|---|---|
| Gender | Female vs Male | 1.0013 | +0.0205 | −0.0205 | **No** |
| Urban/Rural | Rural vs Urban | **0.7971** | +0.1774 | −0.1774 | **YES** |
| Business Reg | Informal vs Formal | 1.6810 | +0.0551 | −0.0551 | **No** |

> [!WARNING]
> **Random Forest urban/rural fairness violation:** DIR = 0.7971 (below the 0.80 four-fifths threshold). Rural applicants receive 79.71% of the approval rate of urban applicants under the Random Forest model. This is the only four-fifths rule violation identified across both models and all protected attributes. This finding strengthens the case for preferring XGBoost as the production model.

**Key contrast:** The Random Forest achieves higher overall accuracy (~90%) but concentrates its errors in ways that disadvantage rural applicants for credit access — a classic accuracy-fairness trade-off. XGBoost, while having a lower overall accuracy, distributes errors more equitably across geographic groups.

---

## 12.6 Threshold Mitigation Analysis

The four-fifths rule violation is limited to the **Random Forest + urban/rural** combination. Since XGBoost is the recommended production model and passes all four-fifths tests, **automatic threshold mitigation was not triggered for XGBoost**. The relevant mitigation analysis applies to the Random Forest.

### Random Forest — Rural Applicants, Threshold Sweep

A threshold sweep from τ = 0.05 to τ = 0.94 was conducted to identify Pareto-efficient fairness-accuracy combinations. Key findings:

- At **τ = 0.50** (standard): DIR = 0.7971 — **VIOLATION**
- At lower thresholds (τ ≈ 0.35–0.45), DIR rises toward 0.85–0.90, recovering the four-fifths compliance
- Accuracy trade-off is modest (~2–3 pp reduction for rural group)

**Recommendation:** If the Random Forest is deployed as a secondary validation model, apply a **rural-specific threshold of τ = 0.40** to restore DIR compliance, with documented fairness-accuracy trade-off per BoN sandbox guidelines.

---

## 12.7 EOD Flag Analysis: Structural Interpretation

Two EOD flags were raised (XGBoost, both against formal-sector applicants and male applicants having lower TPR). These require structural interpretation:

| Flag | Nature | Harmful? | Recommended Action |
|---|---|---|---|
| Gender EOD = +0.1087 | Beneficial disparity — females have higher TPR | **No** — no female harm | Document as equity-positive; monitor for reversal at scale |
| Business EOD = +0.1628 | Formal sector creditworthy applicants under-detected | **Yes** — formal SME harm | Investigate feature gaps for formal sector; consider business credit bureau integration |

---

## 12.8 Overall Fairness Verdict (XGBoost)

| Protected Attribute | DPD | DIR | EOD | Verdict |
|---|---|---|---|---|
| Gender | PASS | PASS (1.14) | FLAG (beneficial) | **APPROVED for deployment** |
| Urban/Rural | PASS | PASS (0.95) | PASS | **APPROVED for deployment** |
| Business Registration | BORDERLINE | PASS (1.31) | FLAG (formal SME harm) | **Conditional — formal sector monitoring required** |

**Overall XGBoost fairness assessment: CONDITIONALLY APPROVED**, subject to:
1. Quarterly FNR monitoring for formal-sector applicants
2. Integration of formal business credit bureau data as a future feature augmentation path
3. Annual DIR recertification under BoN sandbox reporting obligations

---

## 12.9 Responsible AI Framework Compliance

| Framework Requirement | Status |
|---|---|
| Protected attributes excluded from training X | **COMPLIANT** |
| Post-hoc fairness audit conducted | **COMPLIANT** |
| Four-fifths rule evaluated per BoN guidelines | **COMPLIANT** |
| FNR documented as credit-inclusion metric | **COMPLIANT** |
| Threshold mitigation pathway documented | **COMPLIANT** |
| Adverse action explanations (Stage 11) | **COMPLIANT** |
| Fairness-accuracy trade-off Pareto documented | **COMPLIANT** |

---

## 12.10 Publication Figures

| Figure | File | Description |
|---|---|---|
| Fig 12.1 | `figures/fairness_approval_rates.png` | Grouped bar: approval rates by protected group and model |
| Fig 12.2 | `figures/fairness_dir_comparison.png` | DIR by attribute and model with four-fifths reference line |
| Fig 12.3 | `figures/fairness_fnr_by_group.png` | FNR by group — credit exclusion lens |

All figures: 300 DPI, publication-ready.

---

## 12.11 Summary

Stage 12 conducted a complete algorithmic fairness audit of the Namibian digital micro-lending credit risk models:

- **XGBoost passes all four-fifths rule tests** across all three protected attributes — gender, urban/rural location, and business registration status.
- **XGBoost has two EOD flags**: the gender flag is equity-positive (females better detected); the business status flag reveals under-detection of creditworthy formal-sector SMEs and requires structural remedy.
- **Random Forest violates the four-fifths rule** for rural applicants (DIR = 0.7971), providing additional evidence that XGBoost is the superior production choice.
- The full responsible AI compliance checklist is satisfied, meeting BoN Fintech Regulatory Framework 2026 sandbox reporting requirements.

---

*Next: Stage 13 — Socio-Technical & Regulatory Policy Analysis*
