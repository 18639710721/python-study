#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2317:37
# @Author : listem
# @File  ：DayDayUp365.py
# @Software: PyCharm
"""
math库

"""

# 3.1  dayup everyday add 0.01 & daydown everyday reduce 0.01
# import math
# dayup = math.pow((1+0.001),365)  # Return x**y (x to the power of y).
# daydown = math.pow((1-0.001),365)
# print(f"dayup:{dayup:.2f},daydown:{daydown:.2f}")   # dayup:1.44,daydown:0.69

# 3.2 add 5‰ & reduce 5‰
# import math
# dayup = math.pow((1+0.005),365)
# daydown = math.pow((1-0.005),365)
# print(f"dayup:{dayup:.2f} daydown:{daydown:.2f}")   #  dayup:6.17 daydown:0.16

# 3.3 学习比前一天好0.01 不学习就减少0.01
# import math
# dayfactor = 0.01
# dayup = math.pow((1+dayfactor),365)
# daydown = math.pow((1-dayfactor),365)
# print(f"dayup:{dayup:.2f},daydown:{daydown:.2f}")   # ayup:37.78,daydown:0.03

# 3.4 workday N * (1+0.01)   非workday N * (1-0.01)
# dayup,dayfactor = 1.0, 0.01
# for i in range(365):
#     if i % 7 in [6,0]:
#         dayup = dayup * (1 - dayfactor)
#     else:
#         dayup = dayup * (1 + dayfactor)
#
# print(f"dayup:{dayup:.2f}")   # dayup 4.63




