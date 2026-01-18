# 🗂️ Automated Course Classification for Stockholm University Administration

This repository contains the code and materials for a NLP project Course, part of the AI and Language graduate programme at Stockholm University. The goal was to develop an automated system for classifying Swedish university courses into disciplinary domains (*utbildningsområden*, UO). UO classification determine state funding allocations.

## Project Overview

Swedish universities must classify courses into predefined disciplinary domains for funding purposes. This project explores machine learning approaches to automatically classify courses (of which some are interdisciplinary) using course descriptions from Stockholm University's database.

### Key Findings

- **KB-BERT** achieves 90.9% subset accuracy for multi-label classification and 92.9% top-1 accuracy for distributional prediction
- Error analysis revealed that many errors reflect administrative conventions (regulatory constraints, program restrictions) rather than content misunderstanding

## Repository Structure

```
├── project-report.pdf          # Full project report
│
├── su-admin-baseline/
│   └── lis070-su-admin-baseline-2025-12-09-final.ipynb
│                                           # TF-IDF baselines (Logistic Regression, Linear SVC)
│
├── su-admin-bert-binary/
│   ├── lis070-su-admin-bert-binary.ipynb   # KB-BERT multi-label classification (cleaned-up)
│   └── lis070-su-admin-bert-binary-not-cleaned-2025-12-31.ipynb                           
│                                           # KB-BERT multi-label classification (original notebook)
├── su-admin-bert-binary/
│   └── lis070-su-admin-bert-binary.ipynb   # KB-BERT multi-label classification
│
│
│
├── su-admin-BERT-dist-pred/
│   └── su-admin-bert-dist-pred-final-20251208-2300.ipynb
│                                           # KB-BERT Label Distribution Learning
│
├── su-admin-lda-topic-model/
│   ├── lis070-su-admin-topic-modeling-20251210-final.ipynb
│   │                                       # LDA topic modeling for validation
│   └── to_expert/
│       └── su_admin_preliminary_findings_and_error_analysis_v2-1-1.pdf
│                                           # Materials prepared for domain expert review
│
├── results_summary.ipynb                   # Presents results
├── su_utils.py                             # Shared utility functions
└── Kursplanekorpus-2023-original-ej-bearb-head50.csv
                                            # Sample data (50 lines)
```

## Methods

### Models Evaluated

| Model | Task | Description |
|-------|------|-------------|
| TF-IDF + Logistic Regression | Baseline | Traditional text classification |
| TF-IDF + Linear SVC | Baseline | Support vector classification |
| KB-BERT (binary) | Multi-label | Swedish BERT for binary UO classification |
| KB-BERT (distributional) | LDL | Predicts percentage distributions across UOs |

- Trained models are available: https://doi.org/10.5281/zenodo.18256018


**KB-BERT** (bert-base-swedish-cased), a Swedish BERT model 

- Model card: https://huggingface.co/KB/bert-base-swedish-cased

### Technical Details

- **Framework**: HuggingFace Transformers, scikit-learn
- **Validation**: Bootstrap hypothesis testing, expert consultation
- **Metrics**: Subset accuracy, Hamming loss, MAE, Jensen-Shannon divergence

## Data

- The dataset consists of course descriptions from Stockholm University's Ladok system with UO classification labels and percentage distributions.
- A 50-line sample is included in this repository.
- Full dataset are available on Zenodo: https://zenodo.org/records/18256018

## Installation

The notebooks were developed on Kaggle with GPU support. To run locally:

```bash
pip install -r requirements.txt

```

## Author

Fredrik Boglind  
LIS070 Project Course, AI and Language Master's programme, Stockholm University  
January 2026

## DOI **UPDATE 2026-01-16:**
- https://doi.org/10.5281/zenodo.18256018 
