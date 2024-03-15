#71countgff.py by Natalia Marin 

#Categorical Data 
#dictionaries can be used to categorize new information 

#creating an empty dictionary 
count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		#line.startswith() is used instead of line[0]
		if line.startswith('#'): continue
		#retrieves feature from the line
		f = line.split()
		feature = f[2]
		#if feaure not in dictionary, creates key in dictionary
		if feature not in count: count[feature] = 0
		count[feature] +=1 
#reports the count of each feature
for f in count.items(): print(f, n)
for k in sorted(count: print(k, count[k]))

#Composition
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
		count[nt] += 1
#Sorting
for k in sorted(count): print(k, count[k])