__author__ = 'zr'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import threading

urlsh = 'http://www.sse.com.cn/js/common/ssesuggestdata.js;pv397c4da0f03a0ce9'
urlYH = 'http://table.finance.yahoo.com/table.csv?s='


def getCSV(code):
    try:
        url = urlYH + code + ".ss"
        filename = "historyData/" + code + ".csv"
        webSource = urllib.request.urlopen(url)
        webSource = webSource.read().decode()
        csvfile = open(filename,'w')
        csvfile.write(webSource)
        csvfile.close()
    except:
        print(code,'-----!!!!error download csv')

with urllib.request.urlopen(urlsh) as webSource:
    webSource = webSource.read().decode()

codeList = webSource.split(';')


for codeData in codeList[1:-2]:
    codeData = re.findall(r'val:"(\d{6})",val2:"(.*?)",val3:"(.*?)"',codeData)
    code, name, alias = codeData[0]
    print(code,name,alias)
    try:
        getCSV(code)
    except:
        getCSV(code)

  #  try:
  #      t = threading.Thread(target=getCSV,args=(code,))
  #      t.start()
  #  except:
  #      print(code+ "---->error to download")
