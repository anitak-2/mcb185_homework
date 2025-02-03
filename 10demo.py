# 10demo.py by Anita Kim

import math

print('hello, again') # greeting

print(1.5e-2) # numbers

# math operators
print(1 + 1) # addition
print(1 - 1) # subtraction
print(2 * 2) # multiplication
print(1 / 2) # division
print(2 ** 3) # exponentiation
print(5 // 2) # division, no remainder
print(5 % 2) # remainder after division
print(5 * (2 + 1)) # parentheses first

# math functions
print(abs(-2)) # absolute value
print(pow(2, 3)) # exponentiation
print(round(3.14159, ndigits=2)) # rounding to 2 decimal places
print(math.ceil(3.14159)) # rounding up
print(math.floor(3.14159)) # rounding down
print(math.log(2)) # log base e
print(math.log2(2)) # log base 2
print(math.log10(2)) # log base 10
print(math.sqrt(4)) # square root
print(math.pow(2, 3)) # exponentiation
print(math.factorial(7)) # factorial

# practice functions
def square_area(a): return a**2
def circumference(r): return math.pi * 2 * r
def volume_sphere(r): return (4/3) * math.pi * r**3
def celsius_to_fahrenheit(c): return c * (9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * (5/9)
def mph_to_kph(m): return m * 1.60934
def kph_to_mph(k): return k * 0.621371
def dna_conc(a, b): return a * b * 50 # a is absorbance at 260 nm, b is dilution factor
def arith_mean(a, b, c): return (a + b + c) / 3
def geo_mean(a, b, c): return (a * b * c)**(1/3)
def harm_mean(a, b, c): return 3 / (1/a + 1/b + 1/c)
def distance(x1, x2, y1, y2): return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# conditionals
a = 2
b = 3
if a == b:
	print('a equals b')
print(a, b)

def is_even(x): # determine if number is even
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

# boolean
c = a == b
print(c)
print(type(c))

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# more practice
def is_integer(x): # determine if number is an integer
	if x % 1 == 0:
		print(x, 'is an integer')
		return x
	else:
		print(x, 'is not an integer')
		return x

is_integer(2.0)

def valid_prob(x): # determine if number is a valid probability
	if x <= 1 and x >=0:
		print(x, 'is a valid probability')
		return x
	else:
		print(x, 'is not a valid probability')
		return x
		
valid_prob(0.5)

def dna_base_weight(b): # return molecular weight of DNA letter
	if b == 'A':
		return '135 g/mol' 
	elif b == 'C':
		return '111 g/mol'
	elif b == 'G':
		return '151 g/mol'
	elif b == 'T':
		return '126 g/mol'
	else:
		return None
		
print(dna_base_weight('A'))

def dna_complement(b): # return nucleotide complement
	if b == 'A':
		return 'T'
	elif b == 'C':
		return 'G'
	elif b == 'G':
		return 'C'
	elif b == 'T':
		return 'A'
	else:
		return None
		
print(dna_complement('B'))

# even more practice
def maximum(a, b, c): # return maximum of three numbers
	if a >= b and a >= c:
		return a
	elif b >= c:
		return b
	else:
		return c
		
print(maximum(5, 2, 5))

def sensitivity(tp, fn): # calculate sensitivity
	return tp / (tp + fn)
	
print(sensitivity(2, 4))

def specificity(tn, fp): # calculate specificity
	return tn / (tn + fp)
	
print(specificity(3, 6))

def f1_score(tp, fp, fn): # calculate F1 score
	precision = (tp / tp + fp)
	true_pos = sensitivity(tp, fn)
	return (2 * precision * true_pos) / (precision + true_pos)
	
print(f1_score(2, 6, 4))

def shannon_entropy(A, C, T, G): # calculate Shannon entropy
	total = A + C + T + G
	if total == 0:
		return 0
	Aentropy = 0
	if A > 0:
		APi = A / total
		A_entropy = -APi * math.log2(APi)
	if A == 0:
		A_entropy = 0
	if C > 0:
		CPi = C / total
		C_entropy = -CPi * math.log2(CPi)
	if C == 0:
		C_entropy = 0
	if G > 0:
		GPi = G / total
		G_entropy = -GPi * math.log2(GPi)
	if G == 0:
		G_entropy = 0
	if T > 0:
		TPi = T / total
		T_entropy = -TPi * math.log2(TPi)
	if T == 0:
		T_entropy = 0
		
	base_entropy = A_entropy + C_entropy + G_entropy + T_entropy
	return base_entropy
	
print(shannon_entropy(0, 10, 10, 10))