# 32stats.py by Anita Kim
import sys
import math

print(len(sys.argv) - 1) # print number of values on the command line

data = []
mini = float(sys.argv[1])
maxi = float(sys.argv[1])
for arg in sys.argv[2:]: # find min and max of values on the command line
	data.append(float(arg))
	for datas in data:
		if datas < mini:
			mini = datas
		if datas > maxi:
			maxi = datas
			
print(mini)
print(maxi)

data_full = []
total = 0
for arg in sys.argv[1:]: # find mean of values on the command line
	data_full.append(float(arg))
for data_point in data_full:
		total += data_point	
avg = total / (len(sys.argv) - 1)
print(avg)

difference_data = []		
for data_point in data_full: # find standard deviation of values on the command line
	squared_diff = (data_point - avg)**2
	difference_data.append(squared_diff)
tot = 0
for val in difference_data:
	tot += val
variance = tot / len(difference_data)
stdv = math.sqrt(variance)
print(stdv)

copy_data = data_full.copy()
copy_data.sort()
if len(copy_data) % 2 == 1: # find median of values on the command line
	median = copy_data[int(len(copy_data) / 2)]
else:
	median = (copy_data[int(len(copy_data) / 2)] + copy_data[int(len(copy_data) / 2 - 1)])/2
print(median)
	

	
	
	
	
