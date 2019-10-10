'''
1
强口令检测
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的
定义是：长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。你可
能需要用多个正则表达式来测试该字符串，以保证它的强度。

2
strip()的正则表达式版本
写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。如果只
传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
则，函数第二个参数指定的字符将从该字符串中去除。
'''

#1
import re
def strongmm(strr):
    #至少8个字符
    eightRegex = re.compile('.{8,}')
    upandlowRegex = re.compile('[a-z]+[A-Z]+')
    numRegex = re.compile(r'\d+')
    if eightRegex.search(strr) and upandlowRegex.search(strr) and numRegex.search(strr):
        print("强口令")
    else:
        print("密码强度不够,长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字")

a = "dasd15AA"

strongmm(a)
#2
import re

def restrip(a, b=None):
    if b is None:
        restripRegex = re.compile(r'^\s+|\s+$')
        print(restripRegex.sub('',a))
    else:
        bdeleRegex = re.compile(b)
        print(bdeleRegex.sub('', a))

restrip("  dsada  asdas11d    ")
restrip("  dsada  asdas11d    ", "11")
