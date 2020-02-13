#!/usr/bin/python
# -*- coding: utf-8 -*-
#csv文件为google文档下载的csv文件

#a = file.columns.values
#处理list中文乱码，改处理结果为unicode类型 
#b = str(a).replace('u\'','\'')
#print b.decode("unicode-escape") 
#----------------------------------------------------------------------#
#pandas获取列的行号  
#1 已知列名：df[df['列名'].isin([相应的值])]
#经测试 该结果为 相应值的一整行
#2未知列名：data[data.iloc[:,0].isin([data_line])] # 第一列某个值的行号
#经测试 该结果为 相应值的一整行
#----------------------------------------------------------------------#
#如下代码，column a为0的index 为1 行号为0
#
#     a   b   c
#
#1   0   2  4
#
#2   1   3  5
#
#import pandas as pd
#import numpy as np
# 
#data_frame = pd.DataFrame({'a':[0,1],'b':[2,3],'c':[4,5]})
#data_frame.index = [1,2]
#print(data_frame)
##   a  b  c
## 1 0  2  4
## 2 1  3  5
#index = data_frame[data_frame.a == 0].index.tolist()  # index
#print(index) # [1]
#row_number = np.where(data_frame.a == 0)[0].tolist() # 行号
#print(row_number) # [0]
#----------------------------------------------------------------------#
#--------------------获取csv指定值的行号及制定列的值-------------------#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import pandas as pd
file = pd.read_csv("test.csv",encoding='utf-8')
df = pd.DataFrame(file)
positive = range(len(df))
reverse = []
a = list(df)
#h_nub = df[df[a[0]].isin(['rj99999'])].index.tolist() # 取不到值 结果为空list
#result_new = df.loc[h_nub[0], a[3]] #该值的类型为unicode 需要用 str()切换
#exit()
with open("bbb.txt", 'r') as src_txt:
    src_list = list(src_txt)

for i in src_list:
    k = i.replace('\n','')
    h_numb = df[df[a[0]].isin([k])].index.tolist()
    reverse = reverse + h_numb 
    positive = list(set(positive) - set(h_numb))

for ii in positive:
    with open("positive.txt", 'a') as positive_txt:
        positive_txt.write(str(df.loc[ii, a[3]]) + "\n")

for kk in reverse:
    with open("reverse.txt", 'a') as reverse_txt:
        reverse_txt.write(str(df.loc[kk, a[3]]) + "\n")
