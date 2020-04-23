# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2316:57
# @Author : listem
# @File  ：TempCovent.py
# @Software: PyCharm

"""
Talk is cheap. Show me the code
import this     # python之 禅
import keyword
keyword.kwlist    # 关键字
"""
def tempConvert(ValueStr):
    if ValueStr[-1] in ["f", "F"]:
        C = (eval(ValueStr[0:-1]) - 32) * 1.8
        print(f"转换后的温度值为{C:.2f}")
    elif ValueStr[-1] in ["c", "C"]:
        F = 1.8 * eval(ValueStr[0:-1]) + 32
        print(f"转换后的温度值为{F:.2f}F")
    else:
        print("输入格式错误")


TempStr = input("请输入带有符号的温度值")
tempConvert(TempStr)  # 调用并传参
