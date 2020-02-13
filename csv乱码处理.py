#!/usr/bin/python
# -*- coding: utf-8 -*-
#csv文件为google文档下载的csv文件
import codecs
import pandas as pd
file = pd.read_csv("test.csv",encoding='utf-8')
df = pd.DataFrame(file)
a = file.columns.values
#处理list中文乱码，改处理结果为unicode类型 
b = str(a).replace('u\'','\'')
print b.decode("unicode-escape")

#改用list函数处理
a = list(df)
for i in a:
	print i #变量i的值为正常的中文值

#pandas获取列的行号  
#1 已知列名：df[df['列名'].isin([相应的值])]

#2未知列名：data[data.iloc[:,0].isin([data_line])] # 第一列某个值的行号
