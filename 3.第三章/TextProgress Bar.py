#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/4/2319:54
# @Author : listem
# @File  ：TextProgress Bar.py
# @Software: PyCharm

"""
获取时间
    time() 浮点数内部时间值  1587646854.9446335
    ctime()  返回字符串易读  Thu Apr 23 21:06:24 2020
    gmtime()   struce_time计算机可处理的时间格式
时间格式化
    strftime()
    strptime() 用strftime获取时间字符串并输出
程序记时
    perf_counter()
    sleep()  休眠
单行动态刷新
    用后打印的字符覆盖之前的字符
    不能print() 换行
    /r 打印后光标回退到之前的位置
    可以通过perf_counter计算算法进行排序的时间
"""
import time
print(time.time())
print(time.ctime())
print(time.ctime())
print(time.gmtime())
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))   # 需要gmtime格式
start = time.perf_counter()
end = time.perf_counter()
print(end - start)


scale = 1000
print("执行开始".center(scale // 2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale // 2, '-'))

# import time
#
# scale = 10
# print("------执行开始------")
# for i in range(scale + 1):
#     a = '*' * i
#     b = '.' * (scale - i)
#     c = (i / scale) * 100
#     print("{:^3.0f}%[{}->{}]".format(c, a, b))    # ^3 居中对齐占3个字符
#     time.sleep(0.5)
# print("------执行结束------")


# 单行动态刷新  带\r的话会有效果的
# import time
# for i in range(101):
#     print(f"\r{i:3}%",end="")
#     time.sleep(0.05)

