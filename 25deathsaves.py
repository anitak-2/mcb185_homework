# 25deathsaves.py by Anita Kim
import random

trials = 1000
die = 0
stable = 0
revive = 0

for i in range(trials):
    failure = 0
    success = 0
    for i in range(5):
        r = random.randint(1, 20)
        if r == 1:
            failure += 2
        elif r <= 9:
            failure += 1
        elif r >= 10 and r < 20:
            success += 1
        elif r == 20:
            revive += 1
            break
            
        if success == 3:
            stable += 1
            break
        if failure >= 3:
            die += 1
            break

die_prob = die / trials
stable_prob = stable / trials
revive_prob = revive / trials

print('Probability of dying:', die_prob)
print('Probability of stabilizing:', stable_prob)
print('Probability of reviving:', revive_prob)