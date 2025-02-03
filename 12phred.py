# 12phred.py by Anita Kim

import math

def char_to_prob(x): # convert Phred symbols into error rates
	if ord(x) >= 33 and ord(x) <= 73:
		ascii_value = ord(x)
		error_rate = 10**-((ascii_value - 33) / 10)
		return error_rate
	else:
		return None
		
print(char_to_prob('A'))
	
def prob_to_char(x): # convert error rates into Phred symbols
	if x <= 0 or x > 1:
		return None
	ascii_value = -10 * math.log10(x) + 33
	letter = chr(int(ascii_value))
	if ord(letter) >= 33 and ord(letter) <= 73:
		return letter
	else:
		return None
		
print(prob_to_char(0.001))