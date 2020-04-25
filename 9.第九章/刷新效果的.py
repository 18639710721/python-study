#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2423:02
# @Author : listem
# @File  ：刷新效果的.py
# @Software: PyCharm

import turtle
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigits(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in reversed(range(date)):
        num = str(i)
        for n in num:
            print(n)
            drawDigits(eval(n))
        turtle.clear()
        s = len(num)
        turtle.fd(-60*s)      # 往回move s * -60
def main():
    turtle.speed(7)
    turtle.penup()
    turtle.pensize(5)
    turtle.color("red")
    drawDate(10)
    turtle.done()
main()
