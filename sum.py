#! /usr/bin/python
# -*- coding: utf8 -*- 

def sum(a,b):
    return a+b


func = sum
r = func(5,6)
print (r)

# 提供默认值
def add(a,b=2):
    return a+b
r=add(1)
print (r)
r=add(1,5)
print (r)

'''

知识点:
•  Python 不用{}来控制程序结构,他强迫你用缩进来写程序,使代码清晰.
•	定义函数方便简单
•	方便好用的range函数

'''
