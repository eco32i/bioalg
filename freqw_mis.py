# -*- coding: utf-8 -*-
"""
Spyder Editor

Coursera Bioinformatics Algorithms Course
Chapter I
Frequent words with mismatches problem

This is a "naive" approach.
"""
#seq = 'CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC'
FILENAME = "/home/ilya/Downloads/dataset_8_4 (1).txt"
#FILENAME = "frequent_words_mismatch_data.txt"

k = 10
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
    seq = lines[0].strip()
    #k = int(lines[2].strip().split()[0])
    #D = int(lines[2].strip().split()[1])
    
cnt = {}
all_kmers = [seq[i:i+k] for i in xrange(0, len(seq)-k+1)]

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
        
        
print ' '.join(freq_kmers)
print max_freq
#for k,v in cnt.items():
#    print '%s\t\t%d' % (k,v)
print "Done."

