#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2414:50
# @Author : listem
# @File  ：七段数码管绘制.py
# @Software: PyCharm

import random
import time

times = eval(input("请输入你需要模拟的次数"))

pick_first_n = 0
pick_chenge_n = 0
start = time.perf_counter()
for i in range(times):
    car = random.randint(0,2)
    pick_first = random.randint(0,2)
    if pick_first == car:
        pick_first_n += 1
    else:
        pick_chenge_n += 1

pick_first_percent = pick_first_n / times  # 不换选择的胜率
pick_chenge_percent = pick_chenge_n / times   # 计算机选择的胜率

print("如果坚持初选，胜率为{:.2f}%".format(pick_first_percent * 100))
print("如果改变初选，胜率为{:.2f}".format(pick_chenge_percent * 100))
print(f"该程序运行的时间为{time.perf_counter()-start}s")
