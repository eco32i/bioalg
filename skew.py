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
data_file = '/home/ilya/Downloads/dataset_7_6.txt'

with open(data_file, 'r') as fi:
    seq = fi.readlines()[0]

c = g = 0
skew = []
c_ = []
g_ = []

min_ = min_idx = 0
minima = {min_idx: min_,}

for i in xrange(len(seq)):
    skew_val = g - c
    skew.append(skew_val)
    if skew_val < min_:
        min_ = skew_val
        min_idx = i
        minima = {min_idx: min_,}
    elif skew_val == min_:
        minima.update({i: min_,})
    if seq[i] == 'C':
        c += 1
    if seq[i] == 'G':
        g += 1

skew.append(g-c)

print ' '.join([str(x) for x in minima.keys()])
