# Autoniversity Administration

This repository contains the code and materials for my LIS070 Project Course at Stockholm University, focused on developing an automated system for classifying Swedish university courses into disciplinary domains (*utbildningsområden*, UO) that determine state funding allocations.

## Project Overview

Swedish universities must classify courses into predefined disciplinary domains for funding purposes. This project explores machine learning approaches to automate this classification task using course descriptions from Stockholm University's Ladok administrative system.

### Key Findings

- **KB-BERT** achieves strong performance: 90.9% subset accuracy for multi-label classification and 92.9% top-1 accuracy for distributional prediction
- **Label Distribution Learning (LDL)** substantially outperforms binary classification with post-hoc normalization (MAE: 1.39 vs 2.75 percentage points)
- Validation confirms the model learns genuine content-based patterns rather than spurious correlations
- Many apparent "errors" reflect administrative conventions (regulatory constraints, program restrictions) rather than content misunderstanding

## Repository Structure

```
├── project-report-final-draft.pdf          # Full project report (TACL format)
├── final-results-su-adm.pdf                # Summary of final results
│
├── su-admin-baseline/
│   └── lis070-su-admin-baseline-2025-12-09-final.ipynb
│                                           # TF-IDF baselines (Logistic Regression, Linear SVC)
│
├── su-admin-bert-binary/
│   └── lis070-su-admin-bert-binary.ipynb   # KB-BERT multi-label classification
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
├── su_utils.py                             # Shared utility functions
└── Kursplanekorpus-2023-original-ej-bearb-head50.csv
                                            # Sample data (50 courses)
```

## Methods

### Models Evaluated

| Model | Task | Description |
|-------|------|-------------|
| TF-IDF + Logistic Regression | Baseline | Traditional text classification |
| TF-IDF + Linear SVC | Baseline | Support vector classification |
| KB-BERT (binary) | Multi-label | Swedish BERT for binary UO classification |
| KB-BERT (distributional) | LDL | Predicts percentage distributions across UOs |

### Technical Details

- **Language Model**: KB/sentence-bert-swedish-cased
- **Framework**: HuggingFace Transformers, scikit-learn
- **Validation**: Bootstrap hypothesis testing, feature ablation, expert consultation
- **Metrics**: Subset accuracy, Hamming loss, MAE, cosine similarity, Jensen-Shannon divergence

## Data

The full dataset consists of course descriptions from Stockholm University's Ladok system with UO classification labels and percentage distributions. Due to data sharing restrictions, only a 50-course sample is included in this repository.

### Disciplinary Domains (Utbildningsområden)

The classification targets include domains such as:
- Humaniora (Humanities)
- Juridik (Law)
- Naturvetenskap (Natural Sciences)
- Samhällsvetenskap (Social Sciences)
- Teknik (Engineering)
- *and others*

## Requirements

The notebooks were developed on Kaggle. Key dependencies:
- transformers
- torch
- scikit-learn
- pandas
- numpy
- gensim (for LDA)

## Acknowledgments

- **Sofia Gustafsson Capková** (SU Administration) — domain expert validation
- Stockholm University, Department of Computer and Systems Sciences

## Author

Fredrik Boglind  
LIS070 Project Course, Stockholm University  
December 2025

## License

This project is submitted as coursework for LIS070.
