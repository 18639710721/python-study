#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2321:47
# @Author : listem
# @File  ：分支和循环.py
# @Software: PyCharm

# 可迭代的对象 str list
# for i in range(1,6,2):
#     print("hello",i)

for i in range(11):
    if i in [0,5,10]:
        print("+ - - - - + - - - - +")
    else:
        print("|         |         |")
