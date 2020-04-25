# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2322:08
# @Author : listem
# @File  ：CalPi.py
# @Software: PyCharm

"""
random
     梅森旋转算法生成伪随机数
     随机种子 --> 梅森旋转算法 --> 伪随机数(游戏中的暴击概率，氪金玩家的抽卡)

一个程序的80的时间都用在10的循环代码上 可以用perf_counter进行优化
计算PI
    random
    time.perf_counter
    darts   正方形内随机撒点总量  飞镖
    hits 采样数   圆面积内的采样数  初始值为0.0
    start
            遍历循环
            随机撒点 x y
            dist 距离  此处指圆的半径
            计算半径并考虑是否在园内 园内就计数循环
            求出园内点和抛点总数的比，*4

"""
# from random import random
# from time import perf_counter

# darts = 1000 * 1000  # 撒点总数为100万
# hits = 0.0
# start = perf_counter()
# for i in range(1, darts + 1):
#     x, y = random(), random()
#     dist = pow(x ** 2 + y ** 2, 0.5)   # 用pow开方  判断半径长度
#     print(dist)
#     if dist <= 1.0:
#         hits += 1
# PI = 4 * (hits/darts)
# print(f"圆周率PI为{PI}")
# print(f"该程序的运行时间为{perf_counter()-start}")

print(pow(2,0.5))
print(pow(0.5,0.5))