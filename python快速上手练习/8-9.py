'''
扩展多重剪贴板
扩展本章中的多重剪贴板程序，增加一个 delete <keyword>命令行参数，它将
从 shelf 中删除一个关键字。然后添加一个 delete 命令行参数，它将删除所有关键字。

8.9.2 疯狂填词
创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本
文件中出现 ADJECTIVE、NOUN、ADVERB 或 VERB 等单词的地方，加上他们自
己的文本。例如，一个文本文件可能看起来像这样：
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
程序将找到这些出现的单词，并提示用户取代它们。
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
以下的文本文件将被创建：
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
结果应该打印到屏幕上，并保存为一个新的文本文件。

8.9.3 正则表达式查找
编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达
式的所有行。结果应该打印到屏幕上。
'''
#1
https://zhuanlan.zhihu.com/p/43715335
#2
import re

with open('./test.txt', 'r') as f:
    txtlist = f.read()
    adj = re.compile('ADJECTIVE')
    noun = re.compile('NOUN')
    adv = re.compile('ADVERB')
    verb = re.compile('VERB')
    txtlist = txtlist.split()
    for i in range(len(txtlist)):
        if adj.search(txtlist[i]) is not None:
            a = input("Enter an adjective:")
            txtlist[i] = adj.sub(a, txtlist[i])
        if noun.search(txtlist[i]) is not None:
            b = input("Enter an noun:")
            txtlist[i] = noun.sub(b, txtlist[i])
        if adv.search(txtlist[i]) is not None:
            c = input("Enter an adverb:")
            txtlist[i] = adv.sub(c, txtlist[i])
        if verb.search(txtlist[i])is not None:
            d = input("Enter an verb:")
            txtlist[i] = verb.sub(d, txtlist[i])
    tt = " ".join(txtlist)
    with open('./new.txt', 'w+') as f:
        f.write(tt)
        
#3

import re
import os
import copy
a = os.listdir('.')
b = []
userRegex = re.compile('NOUN')
txtRegex = re.compile('\.txt$')
for i in a:
	if txtRegex.search(i) is not None:
		b.append(i)	

for i in b:
	with open('./' + i, 'r') as f1:
		for line in f1:
			if userRegex.search(line) is not None:
				print(line)
	
     
        
        
        
        
        
        
        
        
        
        