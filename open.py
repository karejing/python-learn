#! /usr/bin/python

spath="D:/download/baa.txt"
f=open(spath,"w") # Opens file for writing.Creates this file doesn't exist.
f.write("First line 1.\n")
f.writelines("First line 2.")

f.close()

f=open(spath,"r") # Opens file for reading

for line in f:
    print("每一行的数据是:%s"%line)

f.close()

'''
知识点:
•  open的参数:r表示读,w写数据,在写之前先清空文件内容,a打开并附加内容.
•	打开文件之后记得关闭
'''
