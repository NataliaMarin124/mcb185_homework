#60demo.py By Natalia Marin Unit 6

import mcb185
import sys

"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))

#Program that counts 5 nucleotides w/ if-elif-else stack
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splitting string into list 
	name     = defwords[0] #establishes unique identifier as name variable
	A        = 0 #initialing here b/c we reset for every seq 
	C        = 0
	G        = 0
	T        = 0
	N        = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
		
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

# List Variation 
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splitting string into list 
	name     = defwords[0] #establishes unique identifier as name variable
	nts      = 'ACTGN' 
	counts   = []	
	for i in range(len(nts)): counts.append(0)
	for nt in seq:
		if   nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:           counts[4] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t') # the :.4f = 4th place value
	print()

#Indexing with str.find()
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splitting string into list 
	name     = defwords[0] #establishes unique identifier as name variable
	nts      = 'ACTGN' 
	counts   = [0] * len(nts)
	for nt in seq:
		idx          = nts.find(nt)
		counts[idx] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()
"""	
#Counting with str.count()
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #splitting string into list 
	name     = defwords[0] #establishes unique identifier as name variable
	nts      = 'ACTGN' 
	print(name, end='\t') #this will print the define line with spaces in between
	for nt in nts:
		print(seq.count(nt)/ len(seq), end='\t')
	print()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	