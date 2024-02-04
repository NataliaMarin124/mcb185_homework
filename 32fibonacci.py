# 31 fibonacci.py   by Natalia Marin

def fibonacci(x):
	i =0
	j = 1
	print(i)
	print(j)
	for n in range(x-2):
		fib = i + j
		print(fib)
		i = j
		j = fib
		
print(fibonacci(11))
		