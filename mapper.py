#!/usr/bin/env python


import sys
import os

indexList = []
index = 1

indexList.append(0)
doc_id = os.environ["map_input_file"]
for line in sys.stdin:
    words = line.split()
    for word in line:
        if word == " ":
            indexList.append(index)
            index += 1
        else:
            index += 1

for i in range(len(indexList)):
    print("%s\t%s:%s" % (words[i],doc_id,indexList[i]))


