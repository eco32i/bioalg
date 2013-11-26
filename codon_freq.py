# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:50:47 2013

Codon frequency

@author: ilya
"""
from collections import Counter

CODONS_FILE = '/home/ilya/Downloads/RNA_codon_table_1.txt'
INPUT = 'VKLFPWFNQY'

def build_codon_table(filename):
    '''
    Builds a dict with aminoacids as keys and sets of codons as values.
    '''
    codons = Counter()
    with open(CODONS_FILE, 'r') as fi:
        for line in fi.readlines():
            try:
                codon, aa = line.split()
                codons[aa] += 1
            except ValueError:
                pass
    return codons

the_table = build_codon_table(CODONS_FILE)
print the_table
res = 1
for aa in INPUT:
    res *= the_table[aa]
    
print res
