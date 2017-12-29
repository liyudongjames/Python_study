# setDefault


import sys
import re

WORD_RE = re.compile(r'\w+')  # \w任意一个字母或数字或下划线，也就是 A~Z,a~z,0~9,_ 中任意一个

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])
