import sys
import os
sys.path.append(os.getcwd()+'\\parent\\child')

print(sys.path)

from a import add_func


print (sys.path)

print ("Import add_func from module a")
print ("Result of 1 plus 2 is: ")
print (add_func(1,2))

'''
知识点:
•  如何定义模块和包
•	如何将模块路径添加到系统路径,以便python找到它们
•	如何得到当前路径
'''
