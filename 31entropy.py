# 31entropy.py by Anita Kim
import sys
import math

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	if f <=0 or f >= 1:
		sys.exit('error: not a probability')
	probs.append(f)
	
total = 0
for p in probs:
	total += p
if not math.isclose(total, 1.0):
	sys.exit('error: sum of probabilities does not equal 1')

h = 0
for p in probs:
	h -= p * math.log2(p)
	
print(f'{h:.4f}')