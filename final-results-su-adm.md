## tfidf-baselines

tfidf-baselines 20251209-1400

```
LogReg metrics: ({'subset_accuracy': 0.8136482939632546, 'micro_f1': 0.8967836871978138, 'macro_f1': 0.8444800057691262, 'hamming_loss': 0.025774278215223097},    label        f1
0   2436  0.949367
1   2434  0.940919
2   2441  0.930748
3   2442  0.919003
4   2439  0.854460
5   2445  0.845771
6   2447  0.830189
7   2438  0.735178
8   2444  0.734940
9   2451  0.704225)
LinearSVC metrics: ({'subset_accuracy': 0.8792650918635171, 'micro_f1': 0.9277703005832212, 'macro_f1': 0.8926912835783638, 'hamming_loss': 0.016902887139107613},    label        f1
0   2441  0.966715
1   2436  0.960526
2   2434  0.956650
3   2442  0.932794
4   2451  0.877193
5   2447  0.868613
6   2439  0.861702
7   2445  0.844444
8   2438  0.839378
9   2444  0.818898
```



____________________________________________________________________________________

## su_admin_BERT_dist_pred

su_admin_BERT_dist_pred 2025-12-08 21:20

```
su_admin_BERT_dist_pred 2025-12-08 21:20
============================================================
FINAL EVALUATION METRICS
============================================================
  eval_loss: 0.2162
  eval_mae_pct: 1.3943
  eval_top1_accuracy: 0.9286
  eval_mean_cosine_sim: 0.9509
  eval_mean_js_divergence: 0.0774
  eval_runtime: 34.9933
  eval_samples_per_second: 54.4390
  eval_steps_per_second: 1.7150
  epoch: 3.0000
```

_________________

```
su_admin_BERT_dist_pred 2025-12-08 23:00
============================================================
FINAL EVALUATION METRICS
============================================================
  eval_loss: 0.2158
  eval_mae_pct: 1.4367
  eval_top1_accuracy: 0.9239
  eval_mean_cosine_sim: 0.9511
  eval_mean_js_divergence: 0.0794
  eval_runtime: 35.3052
  eval_samples_per_second: 53.9580
  eval_steps_per_second: 1.6990
  epoch: 3.0000

Per-Label MAE (percentage points):
 uo_code uo_name  mae_pct
    2442      SA 4.222667
    2434      HU 2.198112
    2441      NA 2.152678
    2438      LU 1.809316
    2447      ÖV 1.460524
    2439      ME 0.742094
    2445      VÅ 0.668917
    2444      TE 0.606430
    2436      JU 0.328126
    2451      VU 0.178244
    
============================================================
METHOD COMPARISON SUMMARY
============================================================

Compare these results with:
1. Binary BERT (post-hoc normalized): 
   - MAE: 2.75, Top-1: 85.1%, Cosine: 0.94

2. Direct Distributional BERT (this model):
   - MAE: 1.44, Top-1: 92.4%, Cosine: 0.9511
```

## lis070-su-admin-BERT-binary 20251210 18:30

____________________________________

```
{'eval_loss': 0.05396690219640732,
 'eval_subset_accuracy': 0.9076115485564304,
 'eval_micro_f1': 0.9354697102721685,
 'eval_macro_f1': 0.9046030552413425,
 'eval_hamming_loss': 0.015433070866141733,
 'eval_runtime': 34.2307,
 'eval_samples_per_second': 55.652,
 'eval_steps_per_second': 1.753,
 'epoch': 3.0}
```

```
==================================================
DISTRIBUTIONAL EVALUATION METRICS
==================================================
Mean Absolute Error (percentage points): 2.79
Mean Cosine Similarity:                  0.9382
Mean Jensen-Shannon Divergence:          0.1915
Top-1 Accuracy (primary label match):    0.8525
```

```
Per-Label MAE (percentage points):
 uo_code  mae_pct
    2442 7.022961
    2434 3.773409
    2441 3.452049
    2438 2.910137
    2447 2.828696
    2444 2.301982
    2439 1.794413
    2445 1.479483
    2436 1.377615
    2451 0.960420
```

```
==================================================
WORST PREDICTIONS (highest MAE)
==================================================

Course ID: 31197
  Gold:      {2447: 100.0}
  Gold dist: [  0.   0.   0.   0.   0.   0.   0.   0. 100.   0.]
  Pred dist: [96.5  0.3  0.4  0.3  0.6  0.4  0.3  0.3  0.5  0.3]
  MAE:       19.91

Course ID: 14747
  Gold:      {2438: 100.0}
  Gold dist: [  0.   0. 100.   0.   0.   0.   0.   0.   0.   0.]
  Pred dist: [96.8  0.3  0.5  0.2  0.4  0.7  0.3  0.2  0.4  0.3]
  MAE:       19.90

Course ID: 14747
  Gold:      {2438: 100.0}
  Gold dist: [  0.   0. 100.   0.   0.   0.   0.   0.   0.   0.]
  Pred dist: [96.8  0.3  0.5  0.2  0.5  0.6  0.3  0.2  0.4  0.3]
  MAE:       19.90

Course ID: 49441
  Gold:      {2436: 100.0}
  Gold dist: [  0. 100.   0.   0.   0.   0.   0.   0.   0.   0.]
  Pred dist: [25.9  0.6  0.4  0.3  0.2 71.4  0.2  0.3  0.4  0.2]
  MAE:       19.88

Course ID: 43983
  Gold:      {2434: 100.0}
  Gold dist: [100.   0.   0.   0.   0.   0.   0.   0.   0.   0.]
  Pred dist: [ 0.6  0.5  0.4 45.6  0.6 49.8  1.1  0.4  0.5  0.5]
  MAE:       19.87

Course ID: 43983
  Gold:      {2434: 100.0}
  Gold dist: [100.   0.   0.   0.   0.   0.   0.   0.   0.   0.]
  Pred dist: [ 0.6  0.5  0.4 45.6  0.6 49.8  1.1  0.4  0.5  0.5]
  MAE:       19.87

Course ID: 26238
  Gold:      {2441: 100.0}
  Gold dist: [  0.   0.   0.   0. 100.   0.   0.   0.   0.   0.]
  Pred dist: [59.2  0.4 29.6  0.4  0.9  1.4  0.3  0.4  6.7  0.8]
  MAE:       19.82

Course ID: 15798
  Gold:      {2447: 100.0}
  Gold dist: [  0.   0.   0.   0.   0.   0.   0.   0. 100.   0.]
  Pred dist: [96.4  0.2  0.4  0.2  0.7  0.5  0.2  0.2  0.9  0.3]
  MAE:       19.82

Course ID: 15798
  Gold:      {2447: 100.0}
  Gold dist: [  0.   0.   0.   0.   0.   0.   0.   0. 100.   0.]
  Pred dist: [96.4  0.2  0.4  0.2  0.7  0.5  0.2  0.2  0.9  0.3]
  MAE:       19.82

Course ID: 26238
  Gold:      {2441: 100.0}
  Gold dist: [  0.   0.   0.   0. 100.   0.   0.   0.   0.   0.]
  Pred dist: [60.6  0.4 29.1  0.3  1.   1.3  0.3  0.4  5.8  0.9]
  MAE:       19.80
```

```
Per-Label MAE with names:
 uo_code uo_name  mae_pct
    2442      SA 7.022961	# Samhällsvetenskap
    2434      HU 3.773409	# Humaniora
    2441      NA 3.452049	# Naturvetenskap
    2438      LU 2.910137	# Lärarutbildning  
    2447      ÖV 2.828696	# Övrigt
    
    2444      TE 2.301982	# Teknik
    2439      ME 1.794413	# Medicin
    2445      VÅ 1.479483	# Vård
    2436      JU 1.377615	# Juridik
   2451      VU 0.960420	# Verksamhetsförlagd utbildning
```

```
============================================================
LABEL CONFUSION ANALYSIS
(When gold is X, model predicts Y instead)
============================================================
 gold_code gold_name  pred_code pred_name  confusion_pct  n_cases
      2444        TE       2442        SA      94.594595       70
      2445        VÅ       2442        SA      85.185185       23
      2439        ME       2442        SA      84.507042       60
      2445        VÅ       2438        LU      14.814815        4
      2438        LU       2442        SA      12.328767        9
```

```

============================================================
OVERALL SUMMARY
============================================================

Primary label distribution (Gold vs Predicted):
  HU                       : Gold= 677, Pred= 671, Diff=  -6
  JU                       : Gold=  77, Pred=  76, Diff=  -1
  LU                       : Gold=  73, Pred=  87, Diff= +14
  ME                       : Gold=  71, Pred=  10, Diff= -61
  NA                       : Gold= 321, Pred= 316, Diff=  -5
  SA                       : Gold= 439, Pred= 588, Diff=+149
  TE                       : Gold=  74, Pred=   0, Diff= -74
  VÅ                       : Gold=  27, Pred=   0, Diff= -27
  ÖV                       : Gold= 123, Pred= 135, Diff= +12
  VU                       : Gold=  23, Pred=  22, Diff=  -1

Per-label primary accuracy:
  HU                       : 96.5% (677 cases)
  JU                       : 93.5% (77 cases)
  LU                       : 82.2% (73 cases)
  ME                       : 14.1% (71 cases)
  NA                       : 91.9% (321 cases)
  SA                       : 90.9% (439 cases)
  TE                       : 0.0% (74 cases)
  VÅ                       : 0.0% (27 cases)
  ÖV                       : 91.9% (123 cases)
  VU                       : 95.7% (23 cases)

```

_________________________________________________________________

### Bootstrap 2025-12-12 

```
======================================================================
COMPARISON 1: Linear SVC vs KB-BERT (Multi-label Classification)
======================================================================

============================================================
Metric: Subset Accuracy (↑ = better)
============================================================
Linear SVC          : 82.94% (95% CI: [81.21, 84.62])
KB-BERT             : 90.76% (95% CI: [89.45, 92.02])
------------------------------------------------------------
Difference (B - A): +7.82% (95% CI: [+6.30, +9.34])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Subset Accuracy (↑ = better)
============================================================
Linear SVC          : 82.94% (95% CI: [81.21, 84.62])
KB-BERT             : 90.76% (95% CI: [89.45, 92.02])
------------------------------------------------------------
Difference (B - A): +7.82% (95% CI: [+6.30, +9.34])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Micro-F1 (↑ = better)
============================================================
Linear SVC          : 89.97% (95% CI: [88.87, 91.02])
KB-BERT             : 93.55% (95% CI: [92.52, 94.52])
------------------------------------------------------------
Difference (B - A): +3.57% (95% CI: [+2.56, +4.58])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Micro-F1 (↑ = better)
============================================================
Linear SVC          : 89.97% (95% CI: [88.87, 91.02])
KB-BERT             : 93.55% (95% CI: [92.52, 94.52])
------------------------------------------------------------
Difference (B - A): +3.57% (95% CI: [+2.56, +4.58])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Macro-F1 (↑ = better)
============================================================
Linear SVC          : 85.77% (95% CI: [83.59, 87.59])
KB-BERT             : 90.46% (95% CI: [88.49, 92.12])
------------------------------------------------------------
Difference (B - A): +4.69% (95% CI: [+3.27, +6.23])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Macro-F1 (↑ = better)
============================================================
Linear SVC          : 85.77% (95% CI: [83.59, 87.59])
KB-BERT             : 90.46% (95% CI: [88.49, 92.12])
------------------------------------------------------------
Difference (B - A): +4.69% (95% CI: [+3.27, +6.23])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Hamming Loss (↓ = better)
============================================================
Linear SVC          : 2.31% (95% CI: [2.07, 2.57])
KB-BERT             : 1.54% (95% CI: [1.31, 1.79])
------------------------------------------------------------
Difference (B - A): -0.77% (95% CI: [-1.00, -0.54])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT

============================================================
Metric: Hamming Loss (↓ = better)
============================================================
Linear SVC          : 2.31% (95% CI: [2.07, 2.57])
KB-BERT             : 1.54% (95% CI: [1.31, 1.79])
------------------------------------------------------------
Difference (B - A): -0.77% (95% CI: [-1.00, -0.54])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: KB-BERT
```

```
======================================================================
COMPARISON 2: BERT Binary vs BERT Distributional (Distribution Prediction)
======================================================================

Note: To run this comparison, you need BERT binary sigmoid probabilities.
These should be saved during BERT binary model inference:
  Y_prob = 1 / (1 + np.exp(-logits))  # sigmoid
  np.save('bert_binary_probs.npy', Y_prob)

============================================================
Metric: Top-1 Accuracy (↑ = better)
============================================================
BERT Binary         : 85.25% (95% CI: [83.62, 86.77])
BERT Distributional : 92.39% (95% CI: [91.18, 93.54])
------------------------------------------------------------
Difference (B - A): +7.14% (95% CI: [+5.83, +8.56])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional

============================================================
Metric: Top-1 Accuracy (↑ = better)
============================================================
BERT Binary         : 85.25% (95% CI: [83.62, 86.77])
BERT Distributional : 92.39% (95% CI: [91.18, 93.54])
------------------------------------------------------------
Difference (B - A): +7.14% (95% CI: [+5.83, +8.56])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional

============================================================
Metric: MAE (percentage points) (↓ = better)
============================================================
BERT Binary         : 2.7901 (95% CI: [2.6109, 2.9757])
BERT Distributional : 1.4367 (95% CI: [1.2597, 1.6191])
------------------------------------------------------------
Difference (B - A): -1.3534 (95% CI: [-1.4668, -1.2402])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional

============================================================
Metric: MAE (percentage points) (↓ = better)
============================================================
BERT Binary         : 2.7901 (95% CI: [2.6109, 2.9757])
BERT Distributional : 1.4367 (95% CI: [1.2597, 1.6191])
------------------------------------------------------------
Difference (B - A): -1.3534 (95% CI: [-1.4668, -1.2402])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional

============================================================
Metric: Mean Cosine Similarity (↑ = better)
============================================================
BERT Binary         : 0.9382 (95% CI: [0.9294, 0.9466])
BERT Distributional : 0.9511 (95% CI: [0.9427, 0.9590])
------------------------------------------------------------
Difference (B - A): +0.0129 (95% CI: [+0.0079, +0.0180])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional

============================================================
Metric: Mean Cosine Similarity (↑ = better)
============================================================
BERT Binary         : 0.9382 (95% CI: [0.9294, 0.9466])
BERT Distributional : 0.9511 (95% CI: [0.9427, 0.9590])
------------------------------------------------------------
Difference (B - A): +0.0129 (95% CI: [+0.0079, +0.0180])
p-value: 0.0002 *
Significant at α=0.05: Yes
Winner: BERT Distributional
```

```
======================================================================
INDIVIDUAL MODEL CONFIDENCE INTERVALS
======================================================================


              Model       Subset Accuracy              Micro-F1              Macro-F1       Hamming Loss
Logistic Regression 77.80% [75.91, 79.69] 87.77% [86.64, 88.86] 83.64% [81.52, 85.49] 3.02% [2.74, 3.31]
         Linear SVC 82.94% [81.21, 84.62] 89.97% [88.87, 91.02] 85.77% [83.59, 87.59] 2.31% [2.07, 2.57]
            KB-BERT 90.76% [89.45, 92.02] 93.55% [92.52, 94.52] 90.46% [88.49, 92.12] 1.54% [1.31, 1.79]


              Model       Subset Accuracy              Micro-F1              Macro-F1       Hamming Loss
Logistic Regression 77.80% [75.91, 79.69] 87.77% [86.64, 88.86] 83.64% [81.52, 85.49] 3.02% [2.74, 3.31]
         Linear SVC 82.94% [81.21, 84.62] 89.97% [88.87, 91.02] 85.77% [83.59, 87.59] 2.31% [2.07, 2.57]
            KB-BERT 90.76% [89.45, 92.02] 93.55% [92.52, 94.52] 90.46% [88.49, 92.12] 1.54% [1.31, 1.79]
```

