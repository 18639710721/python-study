#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2517:31
# @Author : listem
# @File  ：汉诺塔.py
# @Software: PyCharm

count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)

hanoi(3,"a","c","b")

