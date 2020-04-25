#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2423:48
# @Author : listem
# @File  ：递归求阶乘.py
# @Software: PyCharm
"""
每次都在计算机内开辟一块内存去调用 
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))