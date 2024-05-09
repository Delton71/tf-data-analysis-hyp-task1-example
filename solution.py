import pandas as pd
import numpy as np
from scipy.stats import binomtest


chat_id = 1265544018 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, 
             y_success: int, y_cnt: int) -> bool:
  
  alpha = 0.08
  res = binomtest(y_success, y_cnt,
                  p=x_success / x_cnt,
                  alternative='greater')
  
  return res.pvalue < alpha
