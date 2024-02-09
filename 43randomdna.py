# 43randomdna.py by Natalia Marin 
# program generates dna seq in FASTA format 
import random

nts = 'AAAT'                                #defines nts programs will use

for i in range(3):                          #will repeat loop 3x
	print(f'>seq-{i+1}', sep='')            #formats >seq-# 
	for r in range(random.randint(20, 60)): #generates random nt seq length
		print(random.choice(nts), end='')   #randomizes the nt order 
	print()                                 #important for proper spacing
	
		
		
	
	
	
