'''
1．写一条 assert 语句，如果变量 spam 是一个小于 10 的整数，就触发AssertionError。
	assert isinstance(spam, int) and spam >= 10 , 'spam mast be a int and large 10'
	
2．编写一条 assert 语句，如果 eggs 和 bacon 包含的字符串彼此相同，而且不
论大小写如何，就触发 AssertionError（也就是说，'hello' 和 'hello' 被认为相同，
'goodbye' 和 'GOODbye' 也被认为相同）。
	assert eggs.upper() != bacon.upper() , 'eggs 和 bacon 包含的字符相同'
	
3．编写一条 assert 语句，总是触发 AssertionError。
	assert False , 'always assertionError'
	
4．为了能调用 logging.debug()，程序中必须加入哪两行代码？
	import logging
	logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

5．为了让 logging.debug() 将日志消息发送到名为 programLog.txt 的文件中，程
序必须加入哪两行代码？
    import logging
    logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    
6．5 个日志级别是什么？
    DEBUG 
    INFO
    WARNING
    ERROR
    CRITICAL

7．你可以加入哪一行代码，禁用程序中所有的日志消息？
    logging.disable(logging.CRITICAL)

8．显示同样的消息，为什么使用日志消息比使用 print() 要好？
    可以禁用日志消息，不必删除日志函数调用。可以选择禁用低级别日志消息。可以创建日志消息。日志消息提供了时间戳。

9．调试控制窗口中的 Step、Over 和 Out 按钮有什么区别？
    Step 按扭让调试器进入函数调用。
    Over 按钮将快速执行函数调用，不会单步进入其中。
    Out 按钮将快速执行余下的代码，直到走出当前所处的函数。
    
10．在点击调试控制窗口中的 Go 按钮后，调试器何时会停下来？
    在点击 Go 后，调试器将在程序末尾或断点处停止。
    
11．什么是断点？
    断点设在一行代码上，在程序执到到达该行时，它导致调试器暂停。
    
12．在 IDLE 中，如何在一行代码上设置断点？
    略
'''

'''
调试硬币抛掷
下面程序的意图是一个简单的硬币抛掷猜测游戏。玩家有两次猜测机会（这
是一个简单的游戏）。但是，程序中有一些缺陷。让程序运行几次，找出缺陷，使
该程序能正确运行。
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''
import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    break
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
print(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

















































