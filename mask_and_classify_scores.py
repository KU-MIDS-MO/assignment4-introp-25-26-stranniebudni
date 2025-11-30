#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 18:54:11 2025

@author: strannie_budni
"""

import numpy as np

def mask_and_classify_scores(arr):
    
    if not isinstance(arr, np.ndarray):
        return None
    
    shape = arr.shape

    if len(shape) != 2:
        return None
    
    x, y = shape
    
    if x != y or y < 4:
        return None
    
    if type(arr) != np.ndarray:
        return None
    
    cleaned = arr.copy()
    cleaned[cleaned < 0] = 0
    cleaned[cleaned > 100] = 100

    levels = np.zeros_like(cleaned, dtype=int)
    medium_mask = (cleaned < 70) & (cleaned >= 40)
    high_mask = cleaned >= 70
    
    levels[medium_mask] = 1
    levels[high_mask] = 2

    
    row_pass_counts = np.zeros(x, dtype=int)
    
    for i in range(x):
        count = 0
        for j in range(y):
            if cleaned[i, j] >= 50:
                count += 1
        row_pass_counts[i] = count
        

    return cleaned, levels, row_pass_counts
