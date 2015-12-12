# -*- coding: utf-8 -*-
### ***input.txt: ***

#  | figure | axes | plot (elements)|
#  |--------|------|-----|
#  |fig = plt.figure([...])|ax = fig.add_axes([left, bottom, width, height])|---|
#  |fig = plt.figure([...])|ax = fig.add_subplot(...)|ax.plot(...)|
#  |fig, ax_array = plt.subplots(...)|fig, ax_array = plt.subplots(...)|ax_array[0][0].hist(...)|
#  |---|---|ax.scatter(...)|
#  |---|---|ax.set_xlabel('x')|
#  |---|---|ax.set_ylabel('y')|
#  |---|---|ax.set_title('title')|
#  |---|---|ax.legend(...)|
#  |---|---|ax.set_xlim(...)|
#  |---|---|ax.set_ylim(...)|
#  |---|---|ax.set_yscale('log')|
#  |---|---|ax.set_xticks(...)|
#  |---|---|ax.set_xticklabels(...)|
#  |---|---|ax.set_yticks(...)|
#  |---|---|ax.set_yticklabels(...)|
#  |---|---|ax.grid(...)|

#  ---

### ***output.txt:***

#  | figure | axes | plot (elements)|
#  |--------|------|-----|
#  |`fig = plt.figure([...])`|`ax = fig.add_axes([left, bottom, width, height])`|`---`|
#  |`fig = plt.figure([...])`|`ax = fig.add_subplot(...)`|`ax.plot(...)`|
#  |`fig, ax_array = plt.subplots(...)`|`fig, ax_array = plt.subplots(...)`|`ax_array[0][0].hist(...)`|
#  |`---`|`---`|`ax.scatter(...)`|
#  |`---`|`---`|`ax.set_xlabel('x')`|
#  |`---`|`---`|`ax.set_ylabel('y')`|
#  |`---`|`---`|`ax.set_title('title')`|
#  |`---`|`---`|`ax.legend(...)`|
#  |`---`|`---`|`ax.set_xlim(...)`|
#  |`---`|`---`|`ax.set_ylim(...)`|
#  |`---`|`---`|`ax.set_yscale('log')`|
#  |`---`|`---`|`ax.set_xticks(...)`|
#  |`---`|`---`|`ax.set_xticklabels(...)`|
#  |`---`|`---`|`ax.set_yticks(...)`|
#  |`---`|`---`|`ax.set_yticklabels(...)`|
#  |`---`|`---`|`ax.grid(...)`|


import os

os.chdir('E:\Python\pandas')

print os.getcwd()

f = open('input.txt')
fw= open('output.txt', 'w')

raw_contents = f.readlines()
new_contents = []

for i in range(len(raw_contents)):
    line = raw_contents[i]
    line_words = line.split('|')

    for j in range(len(line_words)):
        if line_words[j] != '' and line_words[j] != '\n':
            line_words[j] = '`' + line_words[j] + '`'

    new_contents.append('|'.join(line_words))

fw.writelines(new_contents)

fw.close()
f.close()