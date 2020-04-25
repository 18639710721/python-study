#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2517:28
# @Author : listem
# @File  ：递归兔子数列.py
# @Software: PyCharm

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(81))