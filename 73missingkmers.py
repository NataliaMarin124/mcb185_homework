#73missingkmers.py by Natalia Marin 

import dogma
import itertools
import mcb185
import sys


fasta = sys.argv[1]

for k in range(4, 10):
	#print('checking', k)
	
	#getting all kmers for all seq
	kcount= {}
	for defline, seq in mcb185.read_fasta(fasta):
		rev_seq = dogma.reversecomp(seq)
		#print(seq[30:])
		#print(rev_seq[30:])

		for i in range(len(rev_seq) -k +1):
			kmer = rev_seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
			#print(kmer)
			
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
	
	#checking all kmers against all possible kmer
	if len(kcount.keys()) == 4**k: continue
	#print(k)
	
	#report missing kmers
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)

	sys.exit()
	
