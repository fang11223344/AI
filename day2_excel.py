import pandas as pd
#读取用例文件，然后拿到ID，测试时间，测试人员和测试结果做一个统计
#现在只统计一个sheet,用例编号是G列，然后测试人员是T列，测试时间是S列，测试结果是U列
df=pd.read_excel("111.xlsx")
print(df)