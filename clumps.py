# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:40:11 2013

Coursera Bioinformatics Algorithms Course
Chapter I
Finding clumps problem


@author: ilya
"""

from collections import Counter

#FILENAME = "/home/ilya/Downloads/stepic_dataset (7).txt"
FILENAME = "/home/ilya/Downloads/E-coli.txt"

def clumps_for_window(win, k=9, t=4):
    cnt = Counter()
    local_clumps = set()
    for kmer in [win[i:i+k] for i in xrange(0, len(win)-k)]:
        cnt[kmer] += 1
    local_clumps.update(
        [kmer for kmer,count in cnt.most_common() if count >= t]
        )
    return local_clumps


with open(FILENAME, 'r') as fi:
    lines = fi.readlines()
    seq = lines[0].strip()
    #k, L, t = (int(x) for x in lines[1].split())
    
k, L, t = 9, 500, 3

clumps = set()
    
for window in [seq[i:i+L] for i in xrange(0,len(seq)-L)]:
    clumps.update(clumps_for_window(window, k, t))
    
print ' '.join([x for x in clumps])
print len(clumps)
print len(seq)
print k,L,t