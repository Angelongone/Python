#!/usr/bin/python3

#迭代的两个基本方法：iter()和next()

list = [1,2,3,4,5]
it = iter(list)
print(next(it))
print(next(it))

#用for语句遍历
for x in it:
    print (x,end=" ")
