# 34birthday.py by Anita Kim
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
shared = 0

for t in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)

	for i in range(people):
		bday = random.randint(0, days-1)
		calendar[bday] += 1

	collision = False
	for day in range(len(calendar)):
		if calendar[day] > 1: collision = True
	
	if collision: shared += 1
print(shared/trials)