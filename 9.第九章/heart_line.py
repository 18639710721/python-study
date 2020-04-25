#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2516:45
# @Author : listem
# @File  ：heart_line.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
'''
首先要知道笛卡尔心形图的极坐标方程：
r = a(1-sint)，这里让a=1
这个是绘制竖着的心形
如果改为cost就会绘制横着的心形
'''
a = plt.subplot(111,projection='polar')
'''
subplot 是创建一个（坐标系）（暂且这么说）
111 的意思是 将整个窗口分为1行1列 把要绘制的图放在第一个图的位置
projection = 'polar'的意思是说  创建极坐标系
'''
t = np.linspace(0,2*np.pi,60)
'''
np.pi 是Π(pai)
这句是说创建一个从零到2Π，等分成六十份的数组
'''
a.plot(t,1-np.sin(t),'-',c='r')
'''
t是参数，绘制 1-sint 的图像
描点用'-'(可以换成别的，比如'+','.')
颜色是b(蓝色)
'''
plt.show()
'''
展示图像
'''