"""
i = 0
while i < 10: 
	print(i)
	i = i + 3
	
print('final value of i is', i)

for i in range(5):
	print(i)
	
for char in 'hello':
print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)
	
for i in range(len(seq)):
	print(seq(i))''' 
	
	
i = 0                       # this is establishing my initial value for i
while True:                 
	i = i + 1               # to 0 I'm adding 1 and this is redefining my definition for i
	print('hey', i)         
	if i == 3: break        # this 'break' statement will cause loop to break when i = 3 

i = 0
while i < 3:                # this means that while i is less than 3, it will be printed
	print(i)                # it report value for i before addition
	i = i + 1
	print('final value of i is', i)    
	
i = 1                       # defining i = 1 as starting value 
while i < 10: 
	print(i)                # will print i value before adding
	i = i + 3				# b/c 3 is added i will change increments of 3 starting at 1
	print('final value of i is', i)
	
for i in range(1, 10, 3):	# will give numbers bw 1-10 in increment of 3
	print(i)			
	
for i in range(0, 6):		# with this range it gave me numbers 0-4 but no 5
	print(i)
	
for i in range(5): 			# this loop give the same info as previous
	print(i)

for i in range(3, 5):		# first value establishes where loop will start
	print(i)


for char in 'hello':		#hello would be the string
	print(char)				#command will print out individual characters in string

seq = 'gaattc'				#defines seq
for nt in seq: 				
	print(nt)				# will print out the nt defined in seq



for nt1 in 'acgt':
	for nt2 in 'acgt':
			if nt1 == nt2: print(nt1, nt2, '+1')
			else:          print(nt1, nt2, '-1')
# will print out nt1 sequence
	# will print out nt2 sequence
			# will compare nt2 to nt1 

limit = 4
for i in range(limit):
	for j in range(i+1, limit):
		print(i+1, j+1)
	
	
s= 'natalia'
"""

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total 

print(gc_comp('ACAGCGAAT'))
print(gc_comp('AGGGGGCCCTTATA'))


def triangle(n):
	tri = 0
	for i in range(n + 1):
		tri = tri + i
	return tri
		
print(triangle(3))

def factorial(f):
	if f == 0: return 1 
	r = 1
	for i in range(1, f + 1):
		r = r * i
	return r
	
print(factorial(3))


		
		

















