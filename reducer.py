from collections import OrderedDict
from sys import stdin
index = {}

for line in stdin:
    word, postings = line.split('\t')

    postings = postings.replace("\n", "")

    doc_id, number = postings.split(':')

    index.setdefault(word,{})
    index[word].setdefault(doc_id, [])

    if word not in index:
        index[word][doc_id] = number
    else:
        index[word][doc_id].append(number)

index = OrderedDict(sorted(index.items(), key=lambda t: t[0]))

for word in index:
    postings_list = ["%s:%s" % (doc_id, index[word][doc_id])
                     for doc_id in index[word]]

    postings = ', '.join(postings_list)
    postings = postings.replace("'", "")
    print('%s\t%s' % (word, postings))
