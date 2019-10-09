"""
1
逗号代码
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将
前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
该能够处理传递给它的任何列表。
------------------------------------------------------------------------------------
字符图网格
假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样：
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
你可以认为 grid[x][y]是一幅“图”在 x、y 坐标处的字符，该图由文本字符组
成。原点(0, 0)在左上角，向右 x 坐标增加，向下 y 坐标增加。
复制前面的网格值，编写代码用它打印出图像。
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
提示 你需要使用循环嵌套循环，打印出 grid[0][0]，然后 grid[1][0]，然后 grid[2][0]，以此
类推，直到 grid[8][0]。这就完成第一行，所以接下来打印换行。然后程序将打印出
grid[0][1]，然后 grid[1][1]，然后 grid[2][1]，以此类推。程序最后将打印出 grid[8][5]。
而且，如果你不希望在每次 print()调用后都自动打印换行，记得向 print()传递
end 关键字参数。
"""
#1
spam = ['apples', 'bananas', 'tofu', 'cats']
def listTostr(spam):
    a = len(spam)
    b = ""
    for i in range(a - 1):
        b = b + spam[i] + ","
    b = b + "and " + spam[-1]
    #print(b)
    return b
listTostr(spam)

#1-2
spam = ['apples', 'bananas', 'tofu', 'cats']
def listTostr(spam):
    spam[-1] = "and " + spam[-1]
    a = ",".join(spam)
    #print(a)
    return a
listTostr(spam)

#2
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

def printxy(grid):
    a = len(grid)
    for i in range(a):
        b = len(grid[i])
        for o in range(b):
            if o == (b - 1):
                print(grid[i][o])
            else:
                print(grid[i][o], end="")

printxy(grid)





















































