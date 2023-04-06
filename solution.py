import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 753487228 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    stat = (x ** 2).sum()
    
    left_edge_chi_squared = chi2.ppf(alpha / 2, 2 * len(x)) 
    right_edge_chi_squared = chi2.ppf(1 - alpha / 2, 2 * len(x))
    
    left_edge_sigma = np.sqrt(stat / (31 * right_edge_chi_squared))
    right_edge_sigma = np.sqrt(stat / (31 * left_edge_chi_squared))
    
    return (left_edge_sigma, right_edge_sigma)
