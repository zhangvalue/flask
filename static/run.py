# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019-06-26 15:39
# * Author : zhangsf
# *===================================*
# name = ("who are you?")
# print ("hello %s" % (name,))
# with open('/Users/zhangsf/Downloads/Licensed.txt', 'r') as textfile:
#     for row in reversed(list((textfile.read()))):
#         print (row)

a = [1, 2, 3]
print(id(a))      # 4540010376


def mutable(a):
    print(id(a))  # 4540010376
    a += [4]
    print(id(a))  # 4540010376


mutable(a)

b = 1
print(id(b))      # 4538493952


def immutable(b):
    print(id(b))  # 4538493952
    b += 1
    print(id(b))  # 4538493984


immutable(b)
