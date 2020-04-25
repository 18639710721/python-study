# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2414:13
# @Author : listem
# @File  ：DrawhollandRadar.py.py
# @Software: PyCharm
"""
1.绘制单个数字对应的数码管
2.获取一串数字，绘制对应的数码管
3.获取当前系统时间，绘制当前的数码管
"""

import turtle
import datetime
def drawGap():    # 绘制数码管的间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):   # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawdigit(digit):   # 根据数字绘制七段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    for i in date:
        if i == "-":
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        elif i == "=":
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            drawdigit(eval(i))





if __name__ == '__main__':
    turtle.setup(850, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime("%Y-%m=%d+"))
    turtle.hideturtle()
    turtle.done()


