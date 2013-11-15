# -*- coding: utf-8 -*-
"""
Spyder Editor

Coursera Bioinformatics Algorithms Course
Chapter I
Frequent words with mismatches problem

This is a "naive" approach.
"""
seq = 'CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT'
FILENAME = "/home/ilya/Downloads/dataset_8_5.txt"
#FILENAME = "frequent_words_mismatch_complement.txt"
D = 3
k = 8

NUC_DICT = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    }

def rc(seq):
    complement = ''.join(
        [NUC_DICT[nuc] for nuc in seq]
        )
    return complement[::-1]


def get_kmers(seq, k):
    return [seq[i:i+k] for i in xrange(0, len(seq)-k+1)]
    
    
def hamming(s1, s2):
    '''
    Computes Hamming distance between s1 and s2.
    '''
    if len(s1) != len(s2):
        raise ValueError('s1 and s2 must be the same length to compute Hamming distance!')
    return sum(ch1 != ch2 for ch1,ch2 in zip(s1, s2))

with open(FILENAME, 'r') as fi:
    lines = fi.readlines()
    seq = lines[0].strip()
    #k = int(lines[2].strip().split()[0])
    #D = int(lines[2].strip().split()[1])


cnt = {}
#all_kmers = [seq[i:i+k] for i in xrange(0, len(seq)-k+1)]
all_kmers = get_kmers(seq, k) + get_kmers(rc(seq), k)

for kmer in all_kmers:
    cnt[kmer] = 0
    for kmer_ in all_kmers:
        if hamming(kmer, kmer_) <= D:
            cnt[kmer] += 1
        
max_freq = max(cnt.values())
freq_kmers = []
for kmer, freq in cnt.items():
    if freq == max_freq:
        freq_kmers.append(kmer)
        
        
for k,v in cnt.items():
    print '%s\t%d' % (k,v)
print max_freq
print ' '.join(freq_kmers)
print "Done."

