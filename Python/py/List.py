#!/sur/bin/python3

list1 = ['Angelong','Python','Java','C']
list2 = [1,2,3,4,5]

print(list1+list2)  #两个数组中的元素合并用"+"
print(list1*2)  #数组中的元素多次打印

del list2[0]   #删除list2中的第一个元素
print(list2)

print(len(list1))   #获取list1的长度

#判断3是否在list2中
print(3 in list2)

#输出倒数第二个元素
print(list1[-2])

#输出list2第二个后面所有的元素
print(list1[1:])

#列表还支持拼接操作
list2 += [6,7,8,9]
print(list2)

#嵌套列表：子列表里创建其它列表
temp = [list1,list2]
print(temp)

#求list2中的最大值
print(max(list2))

#求list2的最小值
print(min(list2))

#在列表末尾添加新的对象
list1.append('Angelong')
print(list1)

#统计某个元素在列表中出现的次数
print(list1.count('Angelong'))

#在列表末尾一次性追加另一个序列中的多个值
list1.extend(list2)
print(list1)

#找出列表中第一个匹配项的索引位置
print(list1.index('Angelong'))

#将对象插入列表
list2.insert(0,1)
print(list2)

#移除列表中的一个元素（默认最后一个元素）并返回该元素的值
print(list1.pop(0))

#移除列表中的某个值的第一匹配项
list2.remove(1)
print(list2)

#反向列表中元素
list2.reverse()
print(list2)

#对原列表进行排序 True降序  Flase升序
list3 = [8,7,4,2,6,4,7,3,]
list3.sort(reverse = True)
print(list3)

#清空列表
list3.clear()
print(list3)

#复制列表
list3 = list1.copy()
print(list3)
