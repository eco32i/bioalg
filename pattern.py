# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:33:45 2013

Coursera Bioinformatics Algorythms Course
Chapter I

Finding matching problem



@author: ilya
"""
from collections import Counter

#FILENAME = "/home/ilya/Downloads/stepic_dataset (4).txt"
FILENAME = "/home/ilya/Downloads/Vibrio_cholerae.txt"
with open(FILENAME, 'r') as fi:
    lines = fi.readlines()
    #pattern = lines[0].strip()
    pattern = 'CTTGATCAT'
    seq = lines[0].strip()
    
#cnt = Counter()
seq_map = {}
k = len(pattern)
for kmer, pos in [(seq[i:i+k], i) for i in xrange(0, len(seq)-k)]:
    if kmer in seq_map:
        seq_map[kmer].append(pos)
    else:
        seq_map[kmer] = [pos,]
    
print ' '.join(
    [str(x) for x in seq_map[pattern]]
    )
