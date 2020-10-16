from scipy.stats import spearmanr
from numpy import argsort
from pandas import Series

def spearman_rank_correlation(x, y):
    rho, pval = spearmanr(x, y)
    
    return rho

def spearman_corr(data, pred_col, target_col, by_col, k=10): 
    corr = data.sort_values(target_col, ascending=False).groupby(by_col).head(k)
    corr = corr.groupby(by_col).apply(
        lambda x: spearman_rank_correlation(x[pred_col], x[target_col])
    ).to_frame(name='corr')
    
    return corr

def precision_at_k(x, y, k):
    if y.sum() > 0:
        idx = argsort(-x)
        pak = y[idx[:k]].sum() / k
    else:
        pak = 0.0
    
    return pak

def recall_at_k(x, y, k):
    if y.sum() > 0:
        idx = argsort(-x)
        rak = y[idx[:k]].sum() / y.sum()
    else:
        rak = 0.0
    
    return rak

def item_precision_recall(x, pred_col, target_col, k):
    item = {}
    item['precision'] = precision_at_k(x[pred_col], x[target_col], k)
    item['recall'] = recall_at_k(x[pred_col], x[target_col], k)

    return Series(item, index=['precision','recall'])

def precision_recall(data, pred_col, target_col, by_col, k=10):
    pr = data.groupby(by_col).apply(item_precision_recall, pred_col, target_col, k)
    
    return pr
