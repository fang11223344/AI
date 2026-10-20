import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,1,7,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20},{'a': 7, 'b': 12, 'c': 30}]
df = pd.DataFrame(data)
print(df.head(1))
print(df.tail(1))
#返回列索引
print(df.columns)
#返回行索引
print(df.index)
#返回第一行的数据
print(df.loc[0])
#返回第二行的数据
print(df.loc[1])
#返回第一行到第二行的数据
print(df.loc[[0,1]])
#显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
print(df.info)
#返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等
print(df.describe())
#data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
#print(data)
#df=pd.read_excel("111.xlsx")
#print(df)
#显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
#print(df.info)