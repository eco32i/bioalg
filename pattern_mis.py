# -*- coding: utf-8 -*-
"""
Spyder Editor

Coursera Bioinformatics Algorithms Course
Chapter I
Pattern with mismatches problem

This is a "naive" approach.
"""

seq = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
pattern = 'ATTCTGGA'

FILENAME = "/home/ilya/Downloads/dataset_8_3 (4).txt"
#FILENAME = "approximate_match_data.txt"
D = 3 # Number of mismatches

def hamming(s1, s2):
    '''
    Computes Hamming distance between s1 and s2.
    '''
    if len(s1) != len(s2):
        raise ValueError('s1 and s2 must be the same length to compute Hamming distance!')
    return sum(ch1 != ch2 for ch1,ch2 in zip(s1, s2))

with open(FILENAME, 'r') as fi:
    lines = fi.readlines()
    pattern = lines[0].strip()
    seq = lines[1].strip()
    D = int(lines[2].strip())
    
seq_map = {}
k = len(pattern)
for kmer, pos in [(seq[i:i+k], i) for i in xrange(0, len(seq)-k+1)]:
    if hamming(kmer, pattern) <= D:
        if kmer in seq_map:
            seq_map[kmer].append(pos)
        else:
            seq_map[kmer] = [pos,]
    
res = ' '.join(
    [' '.join([str(x) for x in v]) for key,v in seq_map.items()]
    )

print ' '.join([str(x) for x in sorted([int(x) for x in res.split()])])
