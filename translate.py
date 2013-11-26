# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:52:56 2013

Protein translation problem

@author: ilya
"""
# RNA codon table is given in RNA_codon_table_1.txt
# in the following format:
# AAA K
# AAC N
# ...
#

#INPUT = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
INPUT = '/home/ilya/Downloads/dataset_18_3.txt'
CODONS_FILE = '/home/ilya/Downloads/RNA_codon_table_1.txt'

def build_codon_table(filename):
    '''
    Builds a dict with aminoacids as keys and sets of codons as values.
    '''
    codons = {}
    with open(CODONS_FILE, 'r') as fi:
        for line in fi.readlines():
            try:
                codon, aa = line.split()
                codons[codon] = aa
            except ValueError:
                print 'STOP:\t%s' % codon
                codons[line.strip()] = ''
    return codons

def get_triplet(seq):
    n = 0
    while 3 * n < len(seq):
        yield seq[n*3:3*(n+1)]
        n += 1
        
the_table = build_codon_table(CODONS_FILE)
with open(INPUT) as fi:
    lines = fi.readlines()
    
input_seq = lines[0]

protein = []
for triplet in get_triplet(input_seq):
    aa = the_table[triplet]
   # print triplet
    if aa:
        protein.append(aa)
    else:
        break

print ''.join(protein)


