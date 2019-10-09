"""5.6.1 好玩游戏的物品清单
你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
家有 1 条绳索、6 个火把、42 枚金币等。
写一个名为 displayInventory()的函数，它接受任何可能的物品清单，并显示如下：
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

提示 你可以使用 for 循环，遍历字典中所有的键。
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
	item_total += v
	print("Total number of items: " + str(item_total))
displayInventory(stuff)
"""
#1 题目答案都给了
"""
列表到字典的函数，针对好玩游戏物品清单
假设征服一条龙的战利品表示为这样的字符串列表：
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
写一个名为 addToInventory(inventory, addedItems)的函数，其中 inventory 参数
是一个字典，表示玩家的物品清单（像前面项目一样），addedItems 参数是一个列表，
就像 dragonLoot。
addToInventory()函数应该返回一个字典，表示更新过的物品清单。请注意，列
表可以包含多个同样的项。你的代码看起来可能像这样：
def addToInventory(inventory, addedItems):
# your code goes here
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
前面的程序（加上前一个项目中的 displayInventory()函数）将输出如下：
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
"""

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        elif i not in inventory:
            inventory[i] = 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
    item_total += v
    print("Total number of items: " + str(item_total))

addToInventory(inv, dragonLoot)
displayInventory(inv)









































