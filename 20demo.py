# 20demo.py by Natalia_Marin 
	
print("hello, again")			#greeting


import math
print(1.5e-2)
print(1+1)
print(1-1)
print(2**3)
print(1/2)
print(5*(2+1))
print(math.pow(2, 3))
print(pow(2, 3))
print(2 ** 0.5)
print(math.sqrt(4))
print(math.sqrt(2))
print(math.log(2))


a = 3							# side of triangle
b = 4							# side of triangle 
c = math.sqrt(a**2 + b**2)		#hypotenuse
print(c)
print(type(a), type(b), type(c), sep=', ') 

import sys 

def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))

def inversions(a,):
	return -(a)
	
print(inversions(-3))
print(inversions(4))
print(inversions(-31))

def area4(a, b):
	return a*b

print(area4(3, 9))
print(area4(4, 8))

def circumcircle(x,):
	return math.pi*(x)
	
print(circumcircle(1))
print(circumcircle(3))

def tocelsius(a,):
	return (5/9)*(a - 32)
	
print(tocelsius(100))
print(tocelsius(83))
print(tocelsius(56))

def tofahrenheit(a,):
	return (a*(9/5))+32
	
print(tofahrenheit(37))
print(tofahrenheit(28))
print(tofahrenheit(13))

def mph_kph(x,):
	return x * 1.609
	
print(mph_kph(35))
print(mph_kph(121))

def kph_mph(x,):
	return x*0.6213
	
print(kph_mph(9))
print(kph_mph(53))



	