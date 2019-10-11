'''
选择性拷贝
编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中

删除不需要的文件
一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。如果你
试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找
到它们。
编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过
100MB 的文件（回忆一下，要获得文件的大小，可以使用 os 模块的 os.path.getsize()）。
将这些文件的绝对路径打印到屏幕上。

消除缺失的编号
编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如 spam001.txt,
spam002.txt 等，并定位缺失的编号（例如存在 spam001.txt 和 spam003.txt，但不存
在 spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号。
作为附加的挑战，编写另一个程序，在一些连续编号的文件中，空出一些编号，
以便加入新的文件

'''
#1
#selectivecopy.py 

#2
import os
import shutil
dirname = "/"
for flodername, subfolders, filenames in os.walk(dirname):
        for i in filenames:
                try:
                        a = os.path.join(flodername, i)
                        b = os.path.getsize(a)
                        b = b // (1024**2)
                        if b >= 100:
                            os.unlink(a)
                except FileNotFoundError:
                        print("文件真实路径不存在")
             
#3
'''
消除缺失的编号
思路：
建两个列表a,b
a 原始文件夹内的文件名称
b 长度等于a的递增后得文件名称
a[i] 与 b[i] 比较 不相等就替换成b[i]
------------------------------------
附加挑战
a = [] #包含原始文件夹内的文件名
b = [] #包含预留的编号
1: 在a列表中依次添加连续的(len(b) + 1) 个元素
2：将文件名b[i] 替换为a[len(a) + 1]文件名
'''








































































