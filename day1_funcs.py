import os
from cleantext import clean
#去掉首尾空白，中间多个空格合成一个空格   中文符号换成英文符号
s1=" qq,...11   22，，，  "
clean_test =clean(s1)
print(clean_test)
#clean_test = s.rstrip()
#将文本变成小写
s2="MY NAME"
clean_test =clean(s2,lower=True)
print(clean_test)
s2="qqqwwddd"
fo = open("demo.txt", "r+")
c=fo.truncate(3)
line1 = fo.readline()
print("Read Line:", line1)
fo.close()
#合并字符串
frist_name = "ada"
second_name = "love"
full_name1 = frist_name + " " + second_name
full_name2 = f"{frist_name}{second_name}"
print(full_name1)
print(full_name2)