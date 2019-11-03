#!/usr/bin/pyton3

def area (width,height):
    return width * height

def print_welcome(name):
    print("welcome",name)


print_welcome("Angelong")
w = 4
h = 5
print("width =",w,"heighe =",h,"area =",area(w,h))

#函数参数的使用不需要指定顺序
def printinfo(name,age):
    print("名字：" ,name)
    print("年龄：" ,age)
    return

printinfo(age = 50,name = "runoob")


#默认参数
def Ang(name , age = 35):
    print("名字：" ,name)
    print("年龄：" ,age)
    return

Ang(name = "Angelong")

#加了*号的参数会以元祖的形式导入
def muble(age1,*vartuple):
    print("输出：")
    print(age1)
    print(vartuple)

muble(21,42,76,89)

#加了两个星号**的参数会以字典的形式导入
def dict1(agr , **vardict):
    print("以字典的形式输出：")
    print(agr)
    print(vardict)

dict1(1,a = 2,b = 3)

#佚名函数 使用：lambda

sum = lambda arg1,arg2:arg1 + arg2
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))
