__author__ = 'zr'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re

urlsh = 'http://www.sse.com.cn/js/common/ssesuggestdata.js;pv397c4da0f03a0ce9'


with urllib.request.urlopen(urlsh) as webSource:
    webSource = webSource.read().decode()

codeList = webSource.split(';')

for codeData in codeList[1:-2]:
    codeData = re.findall(r'val:"(\d{6})",val2:"(.*?)",val3:"(.*?)"',codeData)
    code, name, alias = codeData[0]
    print(code,name,alias)