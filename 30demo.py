# 30demo.py by Anita Kim
import math

# Strings
s = 'hello world'
print(s)
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
print('hey "dude" don\'t tell me what to do')

# Method Syntax
print(s.upper())
print(s)
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# String Formatting
print(f'{math.pi}') # does nothing special
print(f'{math.pi:.3f}') # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}') # exponent notation
print(f'{"hello world":>20}') # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}') # left justify
print('{} {:.3f}'.format('str.format', math.pi))
print('%s %.3f' % ('printf', math.pi))

# Indexes
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
# Slices
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5]) # both ACBCDE
print(s[5:len(s)], s[5:]) # both FGHIJ
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
# Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)
# s[0] = 'C' generates error
# tax[0] = 'human' generates error
print(tax[0]) # index
print(tax[::-1]) # slice

# enumerate()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
# zip()
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
# Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)
last = nts.pop()
print(last)
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list()
items = list()
print(items)
items.append('eggs')
print(items)
stuff = []
stuff.append(3)
print(stuff)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# split() and join()
text = 'good day          to you'
words = text.split()
print(words)
line = '1.41,2.72,3.14'
print(line.split(','))
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
print('index G?', alph.index('G'))
#print('index Z?', alph.index('Z'))
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Practice Problems
def min_list(n): # returns the minimum value of a list
	n.sort()
	return n[0]
	
numbers = [2, 3, 1, 9, 6]
print(min_list(numbers))

def min_and_max(n): # returns minimum and maximum values of a list
	n.sort()
	return n[0], n[len(n) - 1]
	
print(min_and_max(numbers))

def mean(vals): # returns mean of values in a list
	total = 0
	for val in vals:
		total += val
	avg = total / len(vals)
	return avg
	
print(mean(numbers))

def entropy(vals): # computes entropy of a probability distribution
	shannon_entropy = 0
	for val in vals:
		if val == 0:
			outcome = 0
		else:
			outcome = val * math.log2(val)
			shannon_entropy += outcome
	return -1 * shannon_entropy
	
data = [0.2, 0.3, 0.5, 0]
print(entropy(data))

def kl_distance(ps, qs): # computes Kullback-Leibler distance between 2 sets of probability distributions
	kl = 0
	for p, q in zip(ps, qs):
		if p == 0 or p == 0 and q == 0:
			distance = 0
		elif q == 0:
			kl = math.inf
		else:
			distance = p * math.log2(p / q)
			kl += distance
	return kl

data1 = [0.2, 0.3, 0.5]
data2 = [0.5, 0.1, 0.4]
print(kl_distance(data1, data2))

# sys.argv
import sys
print(sys.argv)

# Converting Types
i = int('42')
x = float('0.61803')
print(i * x)
# x = float('hello')

# Pairwise Comparison
#for i in range(0, len(list)): all combinations
#	for j in range(0, len(list)):

#for i in range(0, len(list)): half-matrix with diagonal
#	for j in range(i, len(list)):
	
#for i in range(0, len(list)): half-matrix without diagonal
#	for j in range(i+1, len(list)):


























