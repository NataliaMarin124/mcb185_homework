import random
random.seed(1)
import sys
import mcb185
import itertools #dont have library
"""
#d = {}      both notations create a dictionary
#d = dict()

#Basics
d = {'dog': 'woof', 'cat': 'meow'}
# adds a new item to dictionary 
d['pig'] = 'oink'
#changes the value of cat from meow to mew
d['cat'] = 'mew'
#deleting an item 
del d['cat']
if 'dog' in d: print(d['dog'])

#Iteration
for key in d:print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

print(d.keys(), d.values(), list(d.values()))


#Lookup Tables

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
    
    
kcount = {}
k = 3
for aas in itertools.product('ACDEFGHIKLMNPQRSTYVWY'):
	print(aas)


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
	
for kmer, n in kcount.itemr():
	print(kmer, n)


size = 10000
words = []
wordd = {}
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
	wordd[token] = True

#print(words)

for i in range(1000):
	if 'MYNAMEISIAN' in words: 
		print('found')


 
def kdh_list(seq):
	aas = 'ARNDCEQGHILMKFPSTWYV'
	kds = (1.8, -4.5, -3.5, -3.5, 2.5, -3.5, -3.5, -0.4 #finish adding aa )
	
	for aa in seq:
		idx = aas.search(aa)
		kdsum += kds[idx]
	return kdsum / len(seq)
	
		
protein_length = 300
protein = [] #makes it into a list 
for i in range(protein_length):
	aa = randome.choice('ACDEFGHIKLMNPQRSTYVWY')
	protein.append(aa)
protein = ''.join(protein)
print(protein)

	for i in range(1000)
	sumh = 0
	for aa in protein:
		sumh += kds(aa)
"""

import itertools
for nts in itertools.product('ACGT', repeat=1):
    print(nts)


