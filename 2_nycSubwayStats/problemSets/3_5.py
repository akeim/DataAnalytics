import numpy as np
import pandas
import statsmodels.api as sm

def compute_r_squared(data, predictions):
    
    top = np.sum((data - predictions)**2)
    bottom = np.sum((data - np.mean(data))**2)
    r_squared = 1 - top/bottom

    return r_squared
