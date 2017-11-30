from sys import stdin
from collections import OrderedDict

index = {}
dictionary = {}


for line in stdin:
    word, postings = line.split('\t')

    postings = postings.replace("\n", "")

    dictionary.setdefault(word, [])
    if word not in dictionary:
        dictionary[word] = postings
    else:
        dictionary[word].append(postings)

ResultDict = OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))

for key, value in ResultDict.iteritems():
    print("{}\t{}").format(key,value)
