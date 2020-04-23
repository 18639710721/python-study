#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2317:08
# @Author : listem
# @File  ：DrawPyhton.py
# @Software: PyCharm

"""
import xxx as x
setup  （width,height,startx,starty） 窗体
penup&pendown  乌龟抬起或者放下
forward(distance)     向前移动  负值为后退

"""
import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()   # 抬起画笔   penup&pendown
turtle.fd(-250)    # 后移了250像素
turtle.pendown()

turtle.pensize(10)    # 设定画笔宽度
turtle.pencolor("purple")  # 画笔颜色
turtle.seth(-40)

for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)

# turtle.circle(40, 80/2)   # 再画个40°的弧形
# turtle.fd(40)
# turtle.circle(16, 180)    # 半径为正的180°弧形
# turtle.fd(40 * 2/3)       # 移动
# turtle.done()
