#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import pandas as pd
file = pd.read_csv("test.csv",encoding='utf-8')
df = pd.DataFrame(file)
a = file.columns.values
#处理list中文乱码
b = str(a).replace('u\'','\'')
print b.decode("unicode-escape")
