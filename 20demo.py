# 20demo.py by Anita Kim

import math
import random

# Tuples
t = 1, 2 # this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
	
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])

# Iteration
#while True:
	#print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	
i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

# for i in range()
for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)
	
for i in range(5):
	print(i)
	
for i in range(0, 5, 1):
	print(i)
	
# for item in container
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
basket = 'milk', 'eggs', 'bread'
for i in range(len(basket)):
	print(basket[i])
	
# Nesting
for i in range(7):
	if i % 2 == 0:  print(i, 'is even')
	else:			print(i, 'is odd')
	
# Practice Problems
def triangular_number(n): # calculate triangular number
	total = 0
	for i in range(1, n+1):
		total = total + i
	return total

print(triangular_number(25))
	
def factorial(n): # calculate factorial
	product = 1
	for i in range(n+1):
		if i == 0:
			product = product
		else:
			product = product * i
	return product
	
print(factorial(8))

def poisson_prob(k, n): # calculate Poisson probability
	poisson_eq = (n**k * math.e**-n) / math.factorial(k)
	return poisson_eq
	
print(poisson_prob(3, 8))

def n_choose_k(n, k): # calculate binomial coefficient
	binomial_eq = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
	return binomial_eq
	
print(n_choose_k(4, 2))

def est_euler(n): # estimate Euler's number
	e = 0
	for i in range(n+1):
		e += (1 / math.factorial(i))
	return e
	
print(est_euler(20))

def is_prime(n): # identify prime numbers
	if n == 0 or n == 1:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True
			
for i in range(51, -1, -1): # practice exam question
	if is_prime(i):
		print(i, end='*\n')
	else:
		print(i)

def est_pi(n): # estimate Pi using Nilakantha series
	pi = 3
	nilakantha = 0
	for i in range(1, n+1):
		if i % 2 == 1:
			nilakantha += (4 / (2*i*(2*i + 1)*(2*i + 2)))
		else:
			nilakantha -= (4 / (2*i*(2*i + 1)*(2*i + 2)))
	pi += nilakantha
	return pi
	
print(est_pi(20))

# Random Numbers
for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))
	
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# More Practice
pi_appr = 0
ins = 0
outs = 0

while True: # estimate Pi using Monte Carlo methods
	x = random.random()
	y = random.random()
	dis = (x ** 2 + y ** 2) ** (0.5)
	in_circle = dis <= 1
	if in_circle:
		ins += 1
	else: outs += 1
	pi_appr = ins / (ins + out) * 4
	print(x, y, dis, ins, outs, pi_appr)

def roll_3D6(): # determine average stat of rolling 3 six-sided dice
	total = 0
	for i in range(3):
		total += random.randint(1, 6)
	avg_stat = total / 3
	return avg_stat
	
print(roll_3D6())

def reroll_3D6():  # determine average stat of rolling 3 six-sided dice with re-rolls for 1's
    total = 0
    for i in range(3):
        roll = random.randint(1, 6)
        while roll == 1:
            roll = random.randint(1, 6)
        total += roll
    avg_stat = total / 3
    return avg_stat

print(reroll_3D6())

def roll_3D6x2():  # determine average stat by rolling pairs of 6-sided dice, taking the maximum each time
    total = 0
    for i in range(3):
        dice1 = random.randint(1, 6) 
        dice2 = random.randint(1, 6) 
        max_roll = max(dice1, dice2)
        total += max_roll
    
    avg_stat = total / 3
    return avg_stat

print(roll_3D6x2())

def droproll_4D6():  # determine average stat by rolling 4 six-sided dice and dropping the lowest
    total = 0
    lowest = 7
    for i in range(4):
    	roll = random.randint(1, 6)
    	total += roll
    	if roll < lowest:
    		lowest = roll
    total -= lowest
    avg_stat = total / 3
    return avg_stat

print(droproll_4D6())
