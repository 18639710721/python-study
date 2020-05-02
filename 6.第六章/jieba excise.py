#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/5/213:05
# @Author : listem
# @File  ：jieba excise.py
# @Software: PyCharm

"""
jinba 中文分词第三方库
    通过图结构和动态规划原理找到最大概率的词组
    精确模式      文本分析
    全模式
    搜素引擎模式
"""

import jieba
print("China is a great country".split())
print(jieba.lcut("中国是一个伟大的国家"))      # 精确模式 返回一个列表类型的分词
print(jieba.lcut("中国是一个伟大的国家",cut_all=True))  # 全模式存在冗余


print(list(jieba.cut("中国是一个伟大的国家")))
print(jieba.add_word("草泥马"))
print(list(jieba.cut("草泥马在青青草原奔腾")))