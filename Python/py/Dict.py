#!/sur/bin/python3

dict1 = {'name':'Angelong','age':20,'addr':'贵州'}
print(dict1)

#访问字典里的值
print(dict1['name'])

#添加信息
dict1['school'] = "菜鸟教程"
print(dict1)
'''
#删除元素与清空字典
del dict1['school']
print(dict1)
dict1.clear()  #清空字典
del dict1      #删除字典
'''
#返回一个字典的浅复制
dict2 = dict1.copy()
print(dict2)

#创建一个新字典，以序列seq中元素做字典的键
seq = ('name','age','addr')
dict2 = dict2.fromkeys(seq)
print(dict2)

#判断键是否在字典中
print('name' in dict1)

#把字典dict1中的键/值对更新到dict3中
dict3 = {}
dict3.update(dict1)
print(dict3)

#删除字典给定的key所对应的值，返回值为被删除的值
dict3.pop('name')
print(dict3)

#随机返回并删除字典中的最后一对键和值
print(dict3.popitem())
