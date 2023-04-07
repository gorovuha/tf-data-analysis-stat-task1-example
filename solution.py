import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    sum = 0
    for i in range(n):
        sum += (i+1)*x[i]
    return sum/n
