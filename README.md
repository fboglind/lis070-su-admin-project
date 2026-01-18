# Automated Course Classification for Stockholm University Administration

This repository contains code and materials for a project in the LIS070 Project Course, part of the AI and Language graduate programme at Stockholm University. The goal was to develop an automated system for classifying Swedish university courses into disciplinary domains (*utbildningsområden*, UO), which determine state funding allocations.

## Key Findings

- **KB-BERT** achieves 90.9% subset accuracy for multi-label classification and 92.4% top-1 accuracy for distributional prediction
- Direct Label Distribution Learning reduces MAE by 48% compared to post-hoc normalization
- Error analysis revealed that many prediction errors reflect administrative conventions (regulatory constraints, program restrictions) rather than content misunderstanding

## Repository Structure

```
├── project-report.pdf                      # Full project report
├── su_utils.py                             # Shared utility functions
├── results_summary.ipynb                   # Results overview
│
├── su-admin-baseline/
│   └── lis070-su-admin-baseline-2025-12-09-final.ipynb
│                                           # TF-IDF baselines (LogReg, Linear SVC)
├── su-admin-bert-binary/
│   ├── lis070-su-admin-bert-binary.ipynb   # KB-BERT multi-label (cleaned)
│   └── lis070-su-admin-bert-binary-not-cleaned-2025-12-31.ipynb
│                                           # KB-BERT multi-label (original)
├── su-admin-BERT-dist-pred/
│   └── su-admin-bert-dist-pred-final-20251208-2300.ipynb
│                                           # KB-BERT Label Distribution Learning
├── su-admin-lda-topic-model/
│   ├── lis070-su-admin-topic-modeling-20251210-final.ipynb
│   │                                       # LDA topic modeling for validation
│   └── to_expert/
│       └── su_admin_preliminary_findings_and_error_analysis_v2-1-1.pdf
│                                           # Materials for domain expert review
│
└── Kursplanekorpus-2023-original-ej-bearb-head50.csv
                                            # Sample data (50 rows)
```

## Models Evaluated

| Model | Task | Performance |
|-------|------|-------------|
| TF-IDF + Logistic Regression | Multi-label baseline | 77.8% subset acc |
| TF-IDF + Linear SVC | Multi-label baseline | 82.9% subset acc |
| KB-BERT (binary) | Multi-label classification | 90.9% subset acc |
| KB-BERT (distributional) | Label Distribution Learning | 92.4% top-1 acc, 1.44 MAE |

All models use [KB-BERT](https://huggingface.co/KB/bert-base-swedish-cased) (bert-base-swedish-cased) as the base Swedish language model.

## Data & Trained Models

The full dataset (course descriptions from Stockholm University's Ladok system) and trained models are available on Zenodo:

**https://doi.org/10.5281/zenodo.18256018**

A 50-row sample is included in this repository for reference.

## Installation

The notebooks were developed on Kaggle with GPU support. To run locally:

```bash
pip install transformers torch scikit-learn pandas gensim
```

## Author

Fredrik Boglind  
LIS070 Project Course, AI and Language Master's Programme  
Stockholm University, January 2026

## **UPDATE 2026-01-16:**
- Data and models is now available here: https://doi.org/10.5281/zenodo.18256018

