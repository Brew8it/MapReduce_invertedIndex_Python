from sys import stdin
from collections import defaultdict

index = {}
dictionary = {}


for line in stdin:
    word, postings = line.split('\t')

    dictionary.setdefault(word, [])

    if word not in dictionary:
        dictionary[word] = postings
    else:
        dictionary[word].append(postings)


for key, value in dictionary.iteritems():
    print("{} , {}").format(key,value)
#print(dictionary['is'])
