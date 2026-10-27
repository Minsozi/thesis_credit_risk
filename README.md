# Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia

**Candidate:** Percyviarance Minsozi Simasiku (Student ID: 201061589)  
**Supervisor:** Mrs. Johanna Nelulu  
**Department:** Department of Computer Science, University of Namibia  
**Degree:** Bachelor of Science in Computer Science (Honours) / Data Science  
**Timeline:** August 2026 – November 2026  

---

## Project Overview
This repository contains the end-to-end research code, datasets, evaluation pipelines, explainability artifacts, and thesis documentation for the study: **"Credit Risk Prediction for Financial Inclusion Using Machine Learning in Namibia"**.

The study investigates whether alternative digital transactional and behavioral data (such as mobile money, airtime recharges, and utility billing) can be utilized by machine learning models to assess credit risk for unbanked, thin-file, and informal business borrowers in Namibia, while ensuring fairness, interpretability, and regulatory alignment with the Bank of Namibia's Regulatory Sandbox.

---

## Repository Structure
```text
thesis_credit_risk/
│
├── data/
│   ├── raw/                  # Original, unedited datasets (with strict licensing & sources)
│   ├── processed/            # Cleaned, encoded, feature-engineered datasets
│   └── external/             # Benchmark data, macroeconomic figures, BoN/NSA reference stats
│
├── notebooks/                # Exploratory data analysis, prototyping, and narrative notebooks
│
├── src/                      # Modular production-quality Python codebase
│   ├── data_cleaning.py      # Profiling, missing value imputation, outlier handling, leakage guards
│   ├── feature_engineering.py# Behavioral feature extraction and encoding
│   ├── train.py              # Stratified cross-validation, baseline and ensemble model training
│   ├── evaluate.py           # Multi-metric evaluation (ROC-AUC, PR-AUC, Brier score, calibration)
│   └── explainability.py     # SHAP, LIME, partial dependence, and demographic fairness audits
│
├── models/                   # Serialized trained models and pipelines (.joblib / .json)
├── figures/                  # Publication-quality charts (ROC curves, PR curves, SHAP summary plots)
├── results/                  # Benchmark comparison tables, metrics logs, fairness audit reports
├── literature/               # Literature matrix, annotated bibliography, policy documents
├── thesis/                   # Draft thesis chapters (Chapters 1 to 6)
├── RESEARCH_LOG.md           # Audit trail of all development decisions, data versions, and milestones
└── README.md                 # Project orientation and reproduction guide
```

---

## Technical Environment & Reproducibility
- **Python Version:** `>= 3.10`
- **Core Libraries:** `numpy`, `pandas`, `scikit-learn`, `xgboost`, `shap`, `lime`, `matplotlib`, `seaborn`
- **Random Seed:** Set globally to `42` across all data splits and stochastic model initializations to guarantee exact reproducibility.
