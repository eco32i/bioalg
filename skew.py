# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:02:29 2013

Coursera Bioinformatics Algorithms Course
Chapter I

Genome skew problem.

This is a "naive" approach.


@author: ilya
"""
#import pandas as pd

seq = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

c = g = 0
c_ = []
g_ = []

for i in xrange(len(seq)):
    c_.append(c)
    g_.append(g)
    if seq[i] == 'C':
        c += 1
    if seq[i] == 'G':
        g += 1

c_.append(c)        
g_.append(g)

res = [x-y for x,y in zip(g_,c_)]
print res

_inc = _dec = False
i = 1
e_ = {}
min_ = 0
while i < len(res):
    if res[i] > res[i-1]:
        if _dec and res[i-1] <= min_:
            min_ = res[i-1]
            e_.update({i-1: min_,})
            #print i-1
        _inc = True
    elif res[i] < res[i-1]:
        _dec = True
    else:
        _inc = _dec = False
    i += 1

print ' '.join([str(k) for k in e_.keys()])
 