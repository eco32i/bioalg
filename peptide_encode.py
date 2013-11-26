# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:52:56 2013

Protein encoding problem.

First, translate 6 ORFs(3 forward, 3 reverse, transcribe first)
Then apply pattern matching algorithm (pattern.py) to it and get the indeces
of matching hits.

Convert those indeces back to DNA coordinates and extract corresponding 
sequences.

@author: ilya
"""
# RNA codon table is given in RNA_codon_table_1.txt
# in the following format:
# AAA K
# AAC N
# ...
#

INPUT = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
#INPUT = '/home/ilya/Downloads/dataset_18_3.txt'
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
                #print 'STOP:\t%s' % codon
                codons[line.strip()] = ''
    return codons

def get_triplet(seq):
    n = 0
    while 3 * n < len(seq):
        yield seq[n*3:3*(n+1)]
        n += 1
        
the_table = build_codon_table(CODONS_FILE)

#with open(INPUT) as fi:
#    lines = fi.readlines()    
#input_seq = lines[0]

def translate(rna, table):
    protein = []
    for triplet in get_triplet(rna):
        aa = table[triplet]
       # print triplet
        if aa:
            protein.append(aa)
        else:
            break
    return ''.join(protein)
    
def get_ORFs(dna):
    ORFs = {}
    rna = dna.replace('T', 'U')
    for i in xrange(3):
        ORFs.update({i: translate(rna[i:]),})
    return ORFs

def get_matching_pos(seq, pattern):
    '''
    Returns a list of positions where pattern appears in seq
    '''
    seq_map = {}
    k = len(pattern)
    for kmer, pos in [(seq[i:i+k], i) for i in xrange(0, len(seq)-k)]:
        if kmer in seq_map:
            seq_map[kmer].append(pos)
        else:
            seq_map[kmer] = [pos,]
    return seq_map[pattern]
    

