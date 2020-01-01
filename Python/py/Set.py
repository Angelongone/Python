#!/sur/bin/python3

set = {'Angelong','Python','Java','Angelong'}
print(set)

#向集合中添加元素
set.add('C')
print(set)

set.update("Temp")
print(set)

#移除集合中的元素
set.remove('C')
print(set)

set.discard('b')
print(set)

#随机删除集合中的一个元素
set.pop()
print(set)

#计算字典的元素个数
print(len(set))
'''
#清空集合
set.clear()
print(set)
'''
#判断元素是否在集合中
print('Java' in set)


