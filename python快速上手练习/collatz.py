"""编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打
印并返回 3 * number + 1。
然后编写一个程序，让用户输入一个整数，并不断对这个数调用 collatz()，直
到函数返回值１（令人惊奇的是，这个序列对于任何整数都有效，利用这个序列，
你迟早会得到 1！既使数学家也不能确定为什么。你的程序在研究所谓的“Collatz
序列”，它有时候被称为“最简单的、不可能的数学问题”）。

这个程序的输出看起来应该像这样：
Enter number:
3
10
5
16
8
4
2
1
-----
输入验证
在前面的项目中添加 try 和 except 语句，检测用户是否输入了一个非整数的字
符串。正常情况下，int()函数在传入一个非整数字符串时，会产生 ValueError 错误，
比如 int('puppy')。在 except 子句中，向用户输出一条信息，告诉他们必须输入一个
整数。
"""

def collatz(number):
    if number % 2 == 0 :
        print(number // 2)
        return number // 2
    elif number % 2 == 1 :
        print(3*number + 1)
        return 3*number + 1

try:
    a = int(input("Enter number:"))
    while a != 1:
        a = collatz(a)
except ValueError:
    print("please enter a digit！")