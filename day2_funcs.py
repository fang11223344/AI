import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,1,7,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
print(data)