# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:01:33 2013
Coursera Bioinformatics Algorythms Course
Chapter I

Reverse complement computation

@author: ilya
"""

FILENAME = '/home/ilya/Downloads/stepic_dataset (2).txt'

NUC_DICT = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    }
    
with open(FILENAME, 'r') as fi:
    seq = fi.readlines()[0].strip()
    
complement = ''.join(
    [NUC_DICT[nuc] for nuc in seq]
    )

rc = complement[::-1]
print rc
print "DONE!"