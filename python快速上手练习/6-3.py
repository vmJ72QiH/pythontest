"""
表格打印
编写一个名为 printTable()的函数，它接受字符串的列表的列表，将它显示在组
织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。例如，
该值可能看起来像这样：
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
你的 printTable()函数将打印出：
apples Alice dogs
oranges Bob cats
cherries Carol moose
banana David goose
提示 :
你的代码首先必须找到每个内层列表中最长的字符串，这样整列就有足够的宽度以
放下所有字符串。你可以将每一列的最大宽度，保存为一个整数的列表。printTable()函
数的开始可以是 colWidths = [0] * len(tableData)，这创建了一个列表，它包含了一些 0，
数目与 tableData 中内层列表的数目相同。这样，colWidths[0]就可以保存 tableData[0]中
最长字符串的宽度，colWidths[1]就可以保存 tableData[1]中最长字符串的宽度，以此类推。
然后可以找到colWidths 列表中最大的值，决定将什么整数宽度传递给rjust()字符串方法。
"""
#python 行转列 推导式解析
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# 使用列表推导
# listb = [[r[col] for r in lista] for col in range(len(lista[0]))]
# print(listb)
listb = []
for col in range(len(lista[0])):
    listc = []
    for r in lista:
        listc.append(r[col])
    listb.append(listc)
print(listb)

-----------------------------------华丽的分割线----------------------------------
#1
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tabledata):
    lista=[[r[col] for r in tabledata] for col in range(len(tabledata[0]))]
    colWidths = [0] * len(tabledata)
    for i in range(len(tabledata)):
        for o in tabledata[i]:
            if len(o) >= colWidths[i]:
                colWidths[i] = len(o)

    for q in range(len(lista)):
        for w in lista[q]:
            if lista[q].index(w) == (len(lista[q]) - 1):
                print(w.rjust(colWidths[lista[q].index(w)]))
            else:
                print(w.rjust(colWidths[lista[q].index(w)]), end=" ")

printTable(tableData)














































