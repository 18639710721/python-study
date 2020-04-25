#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2414:17
# @Author : listem
# @File  ：fact.py
# @Software: PyCharm
"""
函数是一段代码的封装  参数是占位符
阶乘 5  即 1*2*3*4*5
把每个数字遍历出来并放在一个初始值为1的变量里面依次相乘
def 定义函数
位置传参和关键字传参
可变参数 *
return返回值可有可无   可以返回要给tuple  (40, 5, 3)
局部变量和全局变量
    两者可以变量名相同但是不同  函数运算结束后，局部变量被释放
    可以使用global保留字在函数内部使用全局变量
    组合数据类型在python中是用指针来创建的 指针指向外部全局变量，修改指针即修改外部全局变量
    lambda  参数：返回值    函数式编程

"""
def fact(n):
    num = 1
    for i in range(1,n+1):   # n+1 包括前面的阶乘
        num *= i    # 1*2*3*4*5
    return num


print(fact(5))

def fact2(n,m=1):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num // m , n, m   # 用整除吧

print(fact2(5,m=3))