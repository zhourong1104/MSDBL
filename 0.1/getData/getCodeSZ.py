__author__ = 'zr'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from getData import chinesePY


urlYH = 'http://table.finance.yahoo.com/table.csv?s='

def getCSV(code):
    try:
        url = urlYH + code + ".sz"
        filename = "historyData/" + code + ".csv"
        webSource = urllib.request.urlopen(url)
        webSource = webSource.read().decode()
        csvfile = open(filename,'w')
        csvfile.write(webSource)
        csvfile.close()
    except:
        print(code,'-----!!!!error download csv')

with open('szgp.csv','r') as file:
    data = file.readlines()



for i in data[1:-1]:
    code,name = i.split(',')
    alias = chinesePY.main(name)
    print(code,name,alias)
    try:
        getCSV(code)
    except:
        getCSV(code)




#if __name__ == "__main__":
#  str_input='欢迎你A'
#  main(str_input)