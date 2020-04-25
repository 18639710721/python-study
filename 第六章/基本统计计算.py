#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2520:49
# @Author : listem
# @File  ：基本统计计算.py
# @Software: PyCharm


from math import sqrt

def getNum():
    nums = []
    iNumStr = input("请输入数字(直接输入回车键退出)")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(直接输入回车键退出)")

    return nums

def mean(numbers):
    s = 0.0
    for nums in numbers:
        s += nums
    return s / len(numbers)

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return sqrt(sdev / (len(numbers)-1))

def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2-1] + new[size//2])/2
    else:
        med = new[size//2]
    return med

n = getNum()
m = mean(n)
print(f"平均值:{m},标准差:{dev(n,m):.2},中位数:{median(n)}")