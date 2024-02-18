#50demo.py by Natalia Marin 

#Indexes Section
seq = 'GAATTCGGTT'     #seq is my string & the ntds are the characters
print(seq[0], seq[1])  #seq[] tells me what is at that position of sequence
print(seq[-1])         #a negative value in seq[] counts from back to front

for nt in seq: print(nt, end=' ')
print()

for i in range(len(seq)): #len() establishes the limit as seq
	print(i, seq[i])

#Slices Section
s ='ABCDEFGHIJ'
print(s[0:5])    #s[::] is a slice and it will print the first 5 letters of s
print(s[0:8:2])  #it will print out the first 8 letters every two letters
print(s[:5])     #will print out the first 5 letters
print(s[5:])     #will print out the last 5 letters
print(s[::-1])   #will print out the entire list in reverse order
print(s[::])     #will print out the entire string

#Tuples Section
tax = ('Homo', 'sapiens', 9606) #this is how you construct a tuple 
print(tax)                      #output will be in parenthesis showing its a tuple
# tuples are containers of values like strings

print(tax[0])    #index
print(tax[::-1]) #slice

def quadratic(a, b, c):
	x1 = (-b+(b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b-(b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
print(quadratic(1, 1, 1))

#enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

i = 0
for nt in nts:
	print(i, nt)
	i += 1

#Lists Section - contents are mutable
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'        #b/c mutable content can be redefined the second letter as G 
print(nts)

nts.append('C')
print(nts)

last = nts.pop()    #removes elements forom the end of a list 
print(last)
print(nts)

nts.sort()          #sorts in alphabetical order
print(nts)

nts.sort(reverse=True) #sorts in reverse alphabetical order 
print(nts)

nucleotides = nts   #same list now it can be called nts or nucleotides
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

#list subsection
items = list()
print(items)
items.append('eggs')
print(items)

stuff =[]
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas= list(alph)
print(aas)

#split() and join() subsection 

text = 'good day to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))

s = '_'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching Section 
if 'A' in alph: print('yay')  #if A is in container it will print yay
if 'a' in alph: print('no')   #if a is in container it will print no 

print('index G?', alph.index('G'))  # it will look for G in the alph list 
print('index Z?', alph.index('Z')) #this function results in error because theres no Z 

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))    # will return -1 if it cant be found

if 'D' in alph: idx = alph.index('D')
print(idx)

#PRACTICE PROBLEMS

#function that returns the minim value of a list


val = 3, 6, 10, 9, 7, 1, 0.2, 29, 31, 20, 16

def minimum(val):
	mini = val[0]             #sets mini to the value at position 0 in the list == 3
	for x in val[1:]:         #starts the loop to compare itself to the mini 
		if x < mini: mini = x
	return mini

def maximum(val):
	maxi = val[0]             
	for y in val[1:]:
		if y > maxi: maxi = y
	return maxi	

def minmax(val):
	maxi = val[0]
	mini = val[0]
	for x in val:
		if x < mini: mini = x
		if x > maxi: maxi = x
	return mini, maxi
	
print(minimum(val))
print(maximum(val))
print(minmax(val))

def mean(val):
	total = 0                  #establishes initial value for total
	for n in val:              #n will loop through val
		total += n             # everytime n loops it gets added to total
	return total /len(val)
	
print(mean(val))

import math 

def entropy(probs):
	h = 0
	for p in probs: 
		if p > 0:              #an if statement so no errors if any values are 0
			h -= p * math.log2(p)
	return h
print(entropy([0.4, 0.7, 0.5, 0]))

def KLD(P, Q):
	d = 0
	for p, q in zip(P, Q): 
		d += p * math.log2(p/q)
	return d
p1 = [0.2, 0.2, 0.3, 0.3]
p2 = [0.3, 0.2, 0.4, 0.1]

print(KLD(p1, p2))
	

















