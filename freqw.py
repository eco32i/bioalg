# -*- coding: utf-8 -*-
"""
Spyder Editor

Coursera Bioinformatics Algorithms Course
Chapter I
Frequent words problem

This is a "naive" approach.
"""
from collections import Counter

FILENAME = "/home/ilya/Downloads/stepic_dataset (1).txt"

with open(FILENAME, 'r') as fi:
    lines = fi.readlines()
    seq = lines[0].strip()
    k = int(lines[1])
    
cnt = Counter()
for kmer in [seq[i:i+k] for i in xrange(0, len(seq)-k)]:
    cnt[kmer] += 1

most_common = cnt.most_common()
most_kmer, most_cnt = most_common[0]
kmers = []
i = 0
while True:
    kmer, count = most_common[i]
    if count == most_cnt:
        kmers.append(kmer)
        i += 1
    else:
        break
        
print ' '.join(kmers)
print k

print most_common
print seq

print "Done."

