# 33birthday.py by Anita Kim
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
shared = 0

for t in range(trials):
	peeps = []
	for i in range(people):
		bday = random.randint(0, 364)
		if bday in peeps:
			shared += 1
			break
		peeps.append(bday)
		
	collision = False
	for i in range(0, len(peeps)):
		for j in range(i+1, len(peeps)):
			if peeps[i] == peeps[j]: collision = True
	if collision: shared += 1
print(shared/trials)
	