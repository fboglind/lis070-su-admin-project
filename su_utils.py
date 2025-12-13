# %% [code]
# %% [code]

import pandas as pd
import numpy as np
import json
import re


from sklearn.metrics import (
    f1_score, accuracy_score, hamming_loss
)
from scipy.spatial.distance import cosine, jensenshannon
#=============================================#
# Helpers for export/import between notebooks #
#=============================================#

def serialize_tuple(t):
    """Convert tuple to JSON string for CSV storage."""
    if isinstance(t, (list, tuple)):
        return json.dumps(list(t))
    return json.dumps([])

def deserialize_tuple(s):
    """Convert JSON string back to tuple."""
    if pd.isna(s) or s == "":
        return ()
    try:
        return tuple(json.loads(s))
    except:
        return ()

#========================================#
# Helpers for cleaning and preprocessing #
#========================================#

CLEAN_REPLACEMENTS = [
    (r'\s+', ' '),            # collapse whitespace
    (r'<[^>]+>', ' '),         # strip HTML tags
]

def join_uo_by_course_version(
    df,
    id_col="id",
    date_col="decision_date",
    uo_col="uo_code",
    pct_col="uo_percentage",
):
    """Combine all rows with same (id, decision_date) into one conceptual row."""

    df = df.copy()

    # Normalize key columns
    df[id_col]  = pd.to_numeric(df[id_col], errors="coerce")
    df[uo_col]  = pd.to_numeric(df[uo_col], errors="coerce")
    df[pct_col] = (
        df[pct_col].astype(str).str.replace(",", ".", regex=False)
                 .pipe(pd.to_numeric, errors="coerce")
    )
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # Drop invalid rows
    df = df.dropna(subset=[id_col, date_col, uo_col])

    # Single groupby does everything:
    #  - packs UOs and pct into tuples
    #  - takes first non-null value for all other columns
    def pack(g):
        uos  = tuple(g[uo_col].dropna().astype(int))
        pcts = tuple(g[pct_col].dropna().astype(float))
        row  = g.iloc[0].copy()        # representative row for metadata
        row["labels_uo"]  = uos
        row["labels_pct"] = pcts
        return row

    out = df.groupby([id_col, date_col], as_index=False).apply(pack)

    # Remove original UO columns (we have labels_uo now)
    out = out.drop(columns=[uo_col, pct_col], errors="ignore")

    return out.reset_index(drop=True)

def normalize_percentage(x):
    """Convert '50', '50,0', 50 → 50.0; invalid → NaN."""
    if pd.isna(x):
        return np.nan
    s = str(x).strip().replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return np.nan


def build_text(row, cols: list) -> str:
    """Combine text columns into one modeling text field."""
    parts = []
    for c in cols:
        val = row.get(c, None)
        if val is not None and str(val).strip():
            parts.append(str(val))
    return "\n".join(parts)

def primary_from_labels(uos, pcts):
    """Given tuples of UOs and percentages, return primary UO (highest pct or first)."""
    # uos and pcts are tuples from join_uo_by_course_version
    if isinstance(uos, (list, tuple)) and len(uos) > 0:
        if isinstance(pcts, (list, tuple)) and len(pcts) == len(uos) and len(pcts) > 0:
            return int(uos[int(np.argmax(pcts))])
        # fallback: no percentages → just use the first label
        return int(uos[0])
    return np.nan

def clean_text(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = s.replace("\r", " ").replace("\n", " ")
    s = re.sub(r"<[^>]+>", " ", s)        # remove HTML/XML-like tags
    s = re.sub(r"\s+", " ", s)            # collapse whitespace
    return s.strip()

#=========================================#
# Helpers for normalizing to distribution
#=========================================#

def make_distribution_target(row, uo_to_idx, num_labels):
    """
    Convert (labels_uo, labels_pct) to a probability distribution.
    
    Returns: np.array of shape (num_labels,) summing to 1.0
    """
    dist = np.zeros(num_labels, dtype=np.float32)
    uos  = row["labels_uo"]
    pcts = row["labels_pct"]
    
    if not isinstance(uos, (list, tuple)) or len(uos) == 0:
        # Uniform distribution (shouldn't happen often)
        return np.ones(num_labels, dtype=np.float32) / num_labels
    
    # Handle missing/mismatched percentages
    if not isinstance(pcts, (list, tuple)) or len(pcts) != len(uos):
        equal_pct = 100.0 / len(uos)
        pcts = [equal_pct] * len(uos)
    
    for uo, pct in zip(uos, pcts):
        if uo in uo_to_idx:
            dist[uo_to_idx[uo]] = pct
    
    # Normalize to sum to 1 (probability distribution)
    total = dist.sum()
    if total > 0:
        dist = dist / total
    else:
        dist = np.ones(num_labels, dtype=np.float32) / num_labels
    
    return dist

def normalize_to_distribution(probs, scale=100):
    """
    Convert sigmoid probabilities to a normalized distribution.
    
    Args:
        probs: array of shape (n_samples, n_labels) with probabilities
        scale: target sum (100 for percentages)
    
    Returns:
        array of same shape, normalized to sum to `scale`
    """
    # Ensure non-negative
    probs = np.maximum(probs, 0)
    
    # Handle all-zero rows
    row_sums = probs.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums == 0, 1, row_sums)  # avoid division by zero
    
    return (probs / row_sums) * scale

#========================#
# Helpers for evaluation #
#========================#

#  eval_distribution and compute_distribution_metrics

def eval_multilabel(Y_true, Y_pred, label_names):
    metrics = {
        'subset_accuracy': accuracy_score(Y_true, Y_pred),                 # exact match on all labels
        'micro_f1':        f1_score(Y_true, Y_pred, average='micro', zero_division=0),
        'macro_f1':        f1_score(Y_true, Y_pred, average='macro', zero_division=0),
        'hamming_loss':    hamming_loss(Y_true, Y_pred),
    }
    per_class_f1 = f1_score(Y_true, Y_pred, average=None, zero_division=0)
    per_label_df = pd.DataFrame({'label': label_names, 'f1': per_class_f1}) \
                     .sort_values('f1', ascending=False).reset_index(drop=True)
    return metrics, per_label_df

def eval_distribution(gold_dist, pred_dist, scale=100):
    """
    Compute distributional similarity metrics between gold and predicted distributions.
    
    Args:
        gold_dist: array of shape (n_samples, n_labels)
        pred_dist: array of shape (n_samples, n_labels)
        scale: if distributions sum to 100, use 100; if sum to 1, use 1
    
    Returns:
        dict with metrics
    """
    # Normalize to probabilities (sum to 1) for metrics that require it
    gold_prob = gold_dist / scale if scale != 1 else gold_dist
    pred_prob = pred_dist / scale if scale != 1 else pred_dist
    
    # MAE in percentage points
    mae = np.abs(gold_dist - pred_dist).mean() * (100 / scale)
    
    # Per-sample MAE
    per_sample_mae = np.abs(gold_dist - pred_dist).mean(axis=1) * (100 / scale)
    
    # Top-1 Accuracy
    gold_top1 = np.argmax(gold_dist, axis=1)
    pred_top1 = np.argmax(pred_dist, axis=1)
    top1_acc = (gold_top1 == pred_top1).mean()
    
    # Cosine Similarity (per sample, then average)
    cosine_sims = [
        1 - cosine(g, p) if g.sum() > 0 and p.sum() > 0 else 0.0
        for g, p in zip(gold_dist, pred_dist)
    ]
    
    # Jensen-Shannon Divergence (per sample, then average)
    js_divs = []
    for g, p in zip(gold_prob, pred_prob):
        g_safe = g + 1e-10
        p_safe = p + 1e-10
        js_divs.append(jensenshannon(g_safe / g_safe.sum(), p_safe / p_safe.sum()))
    
    return {
        "mae_pct": mae,
        "top1_accuracy": top1_acc,
        "mean_cosine_sim": np.mean(cosine_sims),
        "mean_js_divergence": np.mean(js_divs),
        "per_sample_mae": per_sample_mae,
    }


def compute_distribution_metrics(eval_pred):
    """
    Wrapper for HuggingFace Trainer callback.
    Per-sample array is useful for error analysis
    but breaks the training loop.
    """
    predictions, labels = eval_pred
    metrics = eval_distribution(labels, predictions, scale=1)
    # Remove per_sample_mae (not needed for Trainer logging)
    del metrics["per_sample_mae"]
    return metrics