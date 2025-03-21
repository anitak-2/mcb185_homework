# 24savingthrows.py by Anita Kim
import random

trials = 100000
dc = 5
sides = 20

for dc in range(5, 16, 5):
	nor = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, sides)
		r2 = random.randint(1, sides)
		if r1 >= dc:
			nor += 1
		if r1 >= dc and r2 >= dc:
			dis += 1
		if r1 >= dc or r2 >= dc: 
			adv += 1
	print(dc, 'normal:', nor/trials, 'disadvantage:', dis/trials, 'advantage:', adv/trials)