#python list 相减
问题描述：假设我有这样两个list
       一个是list1，list1 = [1, 2, 3, 4, 5
       一个是list2，list2 = [1, 4, 5]
       我们如何得到一个新的list，list3
       list3中包括所有不在list2中出现的list1中的元素
       即：list3 = list1 - lis
解决方案：我们可以用set（集合）操
       list3 = list(set(list1) - set(list2
       set操作会将一个list转换成一个集合
       假设：list_t = [1, 2, 3, 1
       那么：list(set(list_t)) = [1, 2, 3
       是的，重复的项会被删除。
https://blog.csdn.net/qq_30468133/article/details/84932428