#! /usr/bin/python

x={'a':'aaa','b':'bbb','c':12}
print (x['a'])
print (x['b'])
print (x['c'])

for key in x:
    print ("Key is %s and value is %s" % (key,x[key]))
    
'''
知识点:

    * 将他当Java的Map来用即可.

'''
