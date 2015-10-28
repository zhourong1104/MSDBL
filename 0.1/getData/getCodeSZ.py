__author__ = 'zr'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from getData import chinesePY


with open('szgp.csv','r') as file:
    data = file.readlines()



for i in data[1:-1]:
    code,name = i.split(',')
    alias = chinesePY.main(name)
    print(code,name,alias)


print(len(data[1:-1]))


#if __name__ == "__main__":
#  str_input='欢迎你A'
#  main(str_input)