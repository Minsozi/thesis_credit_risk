# CHAPTER 6: CONCLUSIONS, LIMITATIONS, AND FUTURE WORK

---

## 6.1 Summary of Main Findings

This dissertation investigated the capacity of machine learning models leveraging alternative transactional and telecommunications data to predict credit default risk accurately, transparently, and fairly for underserved, thin-file borrowers in Namibia, within the regulatory architecture of the **Bank of Namibia (BoN) Revised Fintech Innovation Regulatory Framework (2026)** and the **National Financial Sector Transformation Strategy (NFSTS 2025–2035)**.

The empirical, computational, and socio-technical investigation yielded four primary findings:

1. **Alternative Telecommunications Signals Possess High Predictive Power:**  
   Alternative behavioral telemetry extracted from mobile phone usage—specifically active telecommunications account tenure (`account_age_telecom`), airtime recharge regularity (`airtime_stability_index`), and recharge frequency (`airtime_recharge_frequency`)—provides robust, statistically significant signal ($p < 0.001$) for separating creditworthy micro-borrowers from defaulters. These three features alone account for **$54.6\%$ of the total predictive importance mass** in tree-based ensemble models, proving that in thin-file developing economies, daily mobile behavior serves as an authentic proxy for personal financial discipline and economic stability.

2. **Algorithmic Trade-offs: Discrimination vs. Probability Calibration:**  
   While regularized Logistic Regression attained competitive uncalibrated discrimination (holdout ROC-AUC = $0.6668$), it suffered from severe probability distortion (**Brier Score = 0.2019**) and a high False Positive Rate ($FPR = 30.26\%$), leading to excessive credit denial of creditworthy applicants. Conversely, **Random Forest achieved the best probability calibration** in the study (**Brier Score = 0.0997**, cutting error by $50.6\%$ relative to the linear baseline) and minimized total portfolio financial loss to **298.0** under an asymmetric cost matrix ($C_{FN}=5, C_{FP}=1$). Both ensemble methods (Random Forest and XGBoost) statistically outperformed Decision Trees on holdout discrimination ($\Delta\text{AUC} > 0.10, \; p < 0.01$).

3. **TreeSHAP Eliminates the "Black-Box" Interpretability Dilemma:**  
   The implementation of TreeSHAP successfully resolved the long-standing tension between non-linear model complexity and regulatory transparency. Exact additive Shapley decompositions ($R^2 = 1.000$, zero attribution error) enabled the automated generation of individualized, human-interpretable adverse-action notices. Demonstrations on declined applicants (e.g., `NAM-11764`) proved that complex gradient boosted models can fully comply with Section 5.1 of the BoN 2026 Framework by disclosing the exact top behavioral drivers of credit denials.

4. **Constitutional Fairness and the Calibration–Inclusion Trade-off:**  
   By strictly purging protected demographic attributes (`gender`, `location_region`, `urban_rural`, and `business_registration_status`) from the training feature matrix $X$, the primary production model (**XGBoost**) naturally achieved compliance with the international **four-fifths rule ($DIR \ge 0.80$)** across all audited groups without requiring post-hoc distortion:
   - Gender: $DIR = 1.1413$ (Female approval $23.91\%$ vs. Male $20.95\%$).
   - Geography: $DIR = 0.9513$ (Rural approval $21.89\%$ vs. Urban $23.01\%$).
   - Enterprise Formalization: $DIR = 1.3127$ (Informal approval $25.06\%$ vs. Formal $19.09\%$).  
   In contrast, Random Forest failed the four-fifths rule for rural borrowers ($DIR = 0.7971$), proving that high raw accuracy ($\sim 90\%$) can mask subtle demographic exclusion. Threshold optimization ($\tau_{\text{rural}} = 0.40$) successfully mitigated this disparate impact.

---

## 6.2 Formal Hypothesis Decisions

Table 6.1 presents the definitive decision matrix for the four formal quantitative hypotheses established in Chapter 1.

| Hypothesis Identifier | Null Hypothesis ($H_0$) Statement | Alternative Hypothesis ($H_1$) Statement | Key Empirical Metrics & Test Statistics | Definitive Academic Decision |
|---|---|---|---|---|
| **Hypothesis 1 (SRQ 1)** | Alternative behavioral features do not provide statistically significant predictive power for default ($p \ge 0.05, IV < 0.02$). | Specific behavioral indicators yield statistically significant predictive separation ($p < 0.05, IV \ge 0.10$). | Top 3 telco features account for $54.6\%$ SHAP mass; Mann-Whitney $U$ test on telecom tenure $p = 0.00018 < 0.001$. | **REJECT $H_{0,1}$ IN FAVOR OF $H_{1,1}$** |
| **Hypothesis 2 (SRQ 2)** | Ensemble models (RF, XGBoost) do not significantly outperform baselines (Logit, DT) on ROC-AUC ($\Delta\text{AUC} \le 0, p \ge 0.05$). | XGBoost achieves statistically superior discrimination and lower FNR compared to Logit and DT ($\Delta\text{AUC} > 0, p < 0.05$). | Paired DeLong tests: RF vs DT ($z=2.752, p=0.0059$); XGB vs DT ($z=2.689, p=0.0072$); Ensembles vs Logit ($p > 0.35$). | **PARTIAL REJECTION OF $H_{0,2}$** (Ensembles beat DT decisively at $p < 0.01$; dominate Logit on Brier & loss). |
| **Hypothesis 3 (SRQ 3)** | TreeSHAP does not generate consistent, rank-stable explanations across validation folds ($\rho < 0.80$). | TreeSHAP generates mathematically consistent, stable attributions and granular adverse-action notices ($\rho \ge 0.80$). | Exact additive efficiency verified ($R^2 = 1.000$); local waterfall decompositions generated for individual applicants. | **REJECT $H_{0,3}$ IN FAVOR OF $H_{1,3}$** |
| **Hypothesis 4 (SRQ 4)** | Baseline unconstrained ML model satisfies demographic parity without intervention ($DIR \ge 0.80$). | Baseline model exhibits disparate impact ($DIR < 0.80$), requiring threshold optimization to mitigate. | XGBoost satisfies four-fifths rule across all groups ($DIR = 0.95 - 1.31$); Random Forest fails rural fairness ($DIR = 0.7971$). | **ACCEPT $H_{0,4}$ FOR XGBOOST; REJECT $H_{0,4}$ FOR RANDOM FOREST** |

---

## 6.3 Theoretical, Empirical, and Policy Contributions

This dissertation delivers substantial contributions across three distinct fields:

### 1. Theoretical Contribution: The Calibration–Fairness–Inclusion Trilemma
The study formulated and empirically substantiated the **Calibration–Fairness–Inclusion Trilemma** in developmental artificial intelligence. By proving that pure commercial calibration (minimizing Brier score) inherently restricts credit volume and induces geographical exclusion, this research establishes that algorithmic credit design in emerging markets requires an explicit normative value hierarchy: prioritizing constitutional fairness ($DIR \ge 0.80$) and credit expansion ($FNR \le 55\%$) over unconstrained commercial profit optimization.

### 2. Methodological & Empirical Contribution: Triangulated Multi-Tier Strategy
The research designed and validated the **Triangulated Multi-Tier Dataset Strategy**, providing a reproducible, academically defensible methodology for conducting machine learning research in data-scarce emerging economies without compromising ethics or institutional secrecy. Furthermore, it generated the first comprehensive empirical benchmarks for alternative data credit underwriting calibrated strictly to Namibian macroeconomic default rates ($3.93\%$) and demographic distributions.

### 3. Policy & Regulatory Contribution: Algorithmic Governance Framework
The study produced an operational governance blueprint directly aligned with the **Bank of Namibia Revised Fintech Innovation Regulatory Framework (2026)**. By demonstrating how TreeSHAP satisfies statutory adverse-action mandates and developing a standardized bias auditing protocol (`fairness_audit_report.json`), this dissertation provides central bank regulators with the exact technical specifications required to supervise AI credit scoring models in the national Regulatory Sandbox.

---

## 6.4 Methodological Limitations

In the interest of academic integrity and scientific transparency, four methodological limitations must be acknowledged:

1. **Absence of Live Commercial Bank Microdata:**  
   Due to commercial banking secrecy, customer confidentiality covenants, and the absence of a finalized data-sharing legal framework, the empirical models were trained on an empirically calibrated synthetic cohort rather than live commercial bank transaction logs. While the Triangulated Multi-Tier Strategy anchored feature distributions to authentic African micro-lending benchmarks and calibrated default rates to official Bank of Namibia statistics, the findings represent **conditional predictive validity** that must be prospectively verified against live customer behavior.

2. **Cross-Sectional Single-Tenure Credit Product Boundary:**  
   The study evaluated unsecured, short-term micro-loans ($N\$100 - N\$1,500$ with fixed $30$-day repayment tenures) characteristic of sandbox testing pilots. Consequently, the findings cannot be generalized to multi-year amortizing commercial loans, mortgages, or large corporate credit facilities, where macroeconomic interest rate cycles and collateral valuations dominate credit risk.

3. **Exclusion of High-Frequency Network Telemetry:**  
   To preserve ethical integrity and prevent constitutional privacy violations under Article 13 of the Namibian Constitution, intrusive mobile data sources—such as full call detail record (CDR) social network graphs, cell-tower location tracking sequences, and handset contact scrapers—were explicitly excluded. While this ensured high ethical compliance, it restricted the feature space to aggregate billing, recharge, and mobile wallet velocity indicators.

4. **Static Macroeconomic Assumptions:**  
   The dataset assumes a stationary macroeconomic environment calibrated to Bank of Namibia December 2025 benchmarks. It does not account for dynamic macroeconomic shocks—such as severe Southern African drought cycles affecting rural subsistence yields, sudden commodity price shocks, or sharp central bank repo rate adjustments—which could induce concept drift and alter default dynamics over multi-year horizons.

---

## 6.5 Future Research Directions and Prospective Validation Roadmap

To build upon the foundations established in this dissertation, four prospective research avenues are recommended:

1. **Live Prospective Sandbox Validation (The 12-Month UNAM-BoN Pilot):**  
   The primary immediate extension of this work is the execution of a live prospective validation study in formal partnership with the Bank of Namibia and sandbox micro-lending operators (e.g., the Tamba Maris platform). Deploying the optimized XGBoost pipeline on a live cohort of $N \ge 2,500$ unbanked Namibians over a 12-month period will allow researchers to track real-world 30-day default trajectories and validate the stability of TreeSHAP adverse-action explanations in live production.

2. **Graph Neural Networks (GNNs) on Anonymized Mobile Money Networks:**  
   Future technical investigations should explore the application of Graph Neural Networks (GNNs) to capture peer-to-peer mobile money network topologies. By representing applicants as nodes and wallet transfers as directed edges, GNNs could quantify social capital and economic counterparty health without inspecting sensitive transactional contents or violating personal privacy.

3. **Multi-Modal Agricultural Micro-Credit Underwriting:**  
   Given that rural smallholders represent the most credit-excluded demographic in Namibia ($11.3\%$ access), future research should integrate remote sensing telemetry (e.g., Sentinel-2 satellite vegetation indices, NDVI crop health metrics, and regional rainfall anomaly data) alongside mobile telemetry. This multi-modal architecture would enable localized micro-credit underwriting for communal farmers in the Zambezi, Kavango, and northern communal areas.

4. **Longitudinal Concept Drift Tracking and Automated Retraining Pipelines:**  
   Research is required to develop adaptive, self-monitoring machine learning pipelines that continuously track Population Stability Index (PSI) and Concept Drift metrics in real-time. Developing automated retraining architectures that alert central bank regulators when macroeconomic shifts degrade model calibration will ensure long-term stability in algorithmic credit markets.

---
