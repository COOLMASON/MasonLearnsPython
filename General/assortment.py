# -*- coding: utf-8 -*-

#  cday3_text.txt 
#  1 key1
#  2 key2
#  3 key1
#  7 key3
#  8 key2
#  10 key1
#  14 key2
#  19 key4
#  20 key1
#  30 key3

#  cday3_result.txt
#  key1 : ['1', '3', '10', '20']
#  key2 : ['2', '8', '14']
#  key3 : ['7', '30']
#  key4 : ['19']

fo = open('cday3_test.txt', 'r')
content = fo.read()
fo.close()

contentlist = content.split('\n')

index = []
key = []
for line in contentlist:
	index.append(line.split()[0])
	key.append(line.split()[1])
index_trans = []
key_trans = []

for term in key:
	if term not in key_trans:
		key_trans.append(term)

for i in range(0, len(key_trans)):
	index_temp = []
	for j in range(0, len(key)):
		if key[j] == key_trans[i]:
			index_temp.append(index[j])
	index_trans.append(index_temp)

file_new = open('cday3_result.txt', 'w')

for i in range(0, len(key_trans)):
	print key_trans[i], index_trans[i]
	inline_str = "%s : %s\n" % (key_trans[i], index_trans[i])
	file_new.write(inline_str)

file_new.close()
