#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2517:18
# @Author : listem
# @File  ：字符串反转.py
# @Software: PyCharm

def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]

print(rvs("马歇尔歇马"),end=",")
print(rvs("华来士来华"))