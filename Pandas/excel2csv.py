# -*- coding: utf-8 -*-

import os
import pandas as pd

path = 'E:\\Python\\pandas'
os.chdir(path)
print os.getcwd()

filenames = os.listdir(path)

#转换编码为unicode作为中间码（unicode只存在在内存中）
for i in range(len(filenames)):
    filenames[i] = filenames[i].decode('gbk') 
  
print '\n'.join(filenames)

fw = open('filenames.txt', 'w')
#转换为最终写入的编码utf8
fw.write('\n'.join(filenames).encode('utf8'))
fw.close()
print str(len(filenames)) + ' files(include directoris) in path ' + path

excelfiles = len([1  for n in filenames if n.endswith('.xlsx') or n.endswith('.xls')])
print str(excelfiles) + ' Excel files Found.'

fileconverted = 0
for n in filenames:
    ns = n.split('.')
    # if n.endswith('.xls') or n.endswith('.xlsx'):

    if len(ns) == 2 and ns[1] in ('xlsx', 'xls'):
        df = pd.read_excel(n)
        df.to_csv(ns[0] + '.csv', index=False, encoding='gbk')
        fileconverted += 1
        print str(fileconverted) + ' of ' + str(excelfiles) + ' Excel files have changed to csv files.'