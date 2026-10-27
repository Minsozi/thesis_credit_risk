# Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![University of Namibia](https://img.shields.io/badge/Institution-UNAM-red.svg)](https://www.unam.edu.na/)

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: `201061589`)  
**Supervisor:** Mrs. Johanna Nelulu  
**Department:** Department of Computing, Mathematical and Statistical Science  
**Faculty:** Faculty of Agriculture, Engineering & Natural Sciences, University of Namibia  
**Degree:** Bachelor of Science in Computer Science (Honours)  
**Regulatory Sandbox Pilot:** Tamba Maris USSD Digital Credit (`*140*555#`)  
**Timeline:** August 2026 – November 2026  

---

## 🎯 Live Interactive Prototype

Experience the machine learning credit scoring engine, TreeSHAP explainability waterfalls, constitutional fairness audits, and the USSD mobile phone simulator:

- **Local Presentation Launcher:** Double-click [`launch_presentation_tool.bat`](launch_presentation_tool.bat) to launch the dashboard at `http://localhost:8501`.
- **Public Web Deployment:** Once deployed to Streamlit Community Cloud, access the live prototype globally from any device via your public URL.
- **One-Click GitHub & Cloud Deployment:** Run [`setup_github_and_deploy.bat`](setup_github_and_deploy.bat) to connect your GitHub account and publish the prototype to the web.

---

## 📄 Academic Dissertation Documents

The complete honours dissertation is formatted strictly in accordance with the official 19-page UNAM Honours Thesis Template:

- **Official UNAM Word Thesis (.docx):** [`thesis/UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.docx`](thesis/UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.docx) *(1.2 MB, Times New Roman, 12pt, 1.5 line spacing, 2.54 cm margins, complete tables, embedded figures, 7 Chapters, Front Matter, and References)*
- **Master Markdown Manuscript (.md):** [`thesis/UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.md`](thesis/UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.md)
- **Modular Chapters (7 Chapters):** Located in [`thesis/chapters/`](thesis/chapters/)
- **Audit Trail & Research Log:** All 15 stages documented in [`RESEARCH_LOG.md`](RESEARCH_LOG.md)

---

## 🔬 Project Overview

In Namibia, over **77% of the adult population** remains excluded from formal credit markets due to a lack of legacy credit bureau histories, collateral, and payslips. Unbanked citizens are frequently forced to borrow from predatory informal lenders (*omashikofolas*) charging usurious interest rates (30% to over 100% per month).

This repository contains the end-to-end research code, datasets, evaluation pipelines, explainability artifacts, and thesis documentation investigating whether alternative digital transactional and behavioral data (such as mobile money velocity, airtime recharge regularity, and telecom account tenure) can enable fair, accurate, and explainable credit risk prediction for thin-file borrowers, in compliance with the **Bank of Namibia (BoN) Revised Fintech Innovation Regulatory Framework (2026)** and the **National Financial Sector Transformation Strategy (NFSTS 2025–2035)**.

---

## 📊 Summary of Key Empirical Findings

1. **Alternative Data Predictive Validity ($p < 0.001$):**  
   Non-traditional telecom tenure (`account_age_telecom`), airtime recharge regularity (`airtime_stability_index`), and top-up frequency (`airtime_recharge_frequency`) account for **54.6% of total model predictive importance mass**.
2. **Operational Performance:**  
   Random Forest achieved superior probability calibration (**Brier Score = 0.0997**, cutting error by 50.6% relative to Logistic Regression) and minimized total portfolio loss to **298.0** under a 5:1 asymmetric cost penalty ($C_{FN}=5, C_{FP}=1$). Ensembles statistically beat Decision Trees on holdout ROC-AUC ($p < 0.01$).
3. **Regulatory Explainability (TreeSHAP):**  
   Exact polynomial-time Shapley attributions ($R^2 = 1.000$) enable automated, plain-language consumer adverse-action notices compliant with BoN Framework Section 5.1.
4. **Constitutional Fairness (Four-Fifths Rule $DIR \ge 0.80$):**  
   XGBoost naturally complies with the four-fifths rule across all demographic groups without post-hoc distortion:
   - **Gender:** $DIR = 1.1413$ (Women receive higher approval rates; equity-positive).
   - **Geography:** $DIR = 0.9513$ (Near-zero rural bias).
   - **Enterprise Status:** $DIR = 1.3127$ (Informal micro-traders strongly supported).
5. **The Calibration–Fairness–Inclusion Trilemma:**  
   Formulates the structural developmental trade-off, recommending that emerging market regulators prioritize **Constitutional Fairness ($DIR \ge 0.80$) and Financial Inclusion ($FNR \le 55\%$) over pure commercial calibration**.

---

## 📁 Repository Structure

```text
thesis_credit_risk/
│
├── app.py                            # Interactive Streamlit presentation prototype
├── launch_presentation_tool.bat      # One-click Windows local launcher
├── setup_github_and_deploy.bat       # One-click GitHub & Streamlit Cloud deployer
├── requirements.txt                  # Python dependencies for cloud deployment
├── .streamlit/config.toml            # Streamlit theme & performance settings
│
├── data/
│   ├── raw/                          # Calibrated Namibian cohort (5,000 instances)
│   ├── processed/                    # Leak-free train/test sets, protected attributes
│   └── data_dictionary.md            # 28-variable data governance dictionary
│
├── models/                           # Serialized machine learning models (.joblib)
│   ├── advanced_xgboost.joblib       # Primary BoN Sandbox production model
│   ├── advanced_random_forest.joblib # Calibrated ensemble model
│   ├── baseline_logistic_regression.joblib
│   ├── baseline_decision_tree.joblib
│   ├── scaler.joblib                 # Leak-free fitted StandardScaler
│   └── feature_columns.joblib
│
├── figures/                          # 300-DPI publication-grade figures
│   ├── roc_curves_comparison.png
│   ├── pr_curves_comparison.png
│   ├── calibration_curves.png
│   ├── cost_curve_threshold_analysis.png
│   ├── shap_feature_importance_bar.png
│   ├── individual_adverse_action_waterfall.png
│   └── fairness_dir_comparison.png
│
├── results/                          # Performance JSONs & CSV benchmarks
│   ├── model_comparison_benchmark.csv
│   ├── statistical_hypothesis_tests.json (DeLong tests)
│   ├── fairness_audit_report.json
│   └── local_adverse_action_explanations.json
│
├── src/                              # Modular production-quality Python codebase
│   ├── data_generation.py            # Calibrated cohort simulation
│   ├── data_cleaning.py              # Winsorization & missingness flags
│   ├── feature_engineering.py        # Ratio construction & leak-free scaling
│   ├── train_baselines.py            # Logistic Regression & Decision Trees
│   ├── train_advanced.py             # Random Forest & XGBoost tuning
│   ├── evaluate.py                   # DeLong tests & cost curve optimization
│   ├── explainability.py             # TreeSHAP waterfalls & global beeswarm
│   ├── fairness_audit.py             # Demographic parity & four-fifths tests
│   └── generate_unam_word_thesis.py  # UNAM Word thesis (.docx) generator
│
├── thesis/                           # Dissertation manuscripts
│   ├── UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.docx  # Official UNAM Word thesis
│   ├── UNAM_Honours_Thesis_Percyviarance_Simasiku_2026.md    # Master 7-chapter Markdown
│   ├── full_thesis_manuscript.md     # Consolidated full manuscript
│   └── chapters/                     # Modular chapter files (Front Matter, Ch 1 to 7)
│
├── RESEARCH_LOG.md                   # Audit trail across all 15 project stages
└── README.md                         # Project orientation and deployment guide
```

---

## 💻 How to Run Locally

1. Clone or download the repository:
   ```bash
   git clone https://github.com/<your-username>/thesis_credit_risk.git
   cd thesis_credit_risk
   ```
2. Set up virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the interactive presentation prototype:
   ```bash
   streamlit run app.py
   ```
   Or double-click `launch_presentation_tool.bat` on Windows.
