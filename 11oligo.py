# 11oligo.py by Anita Kim

def oligo_melt(A, C, G, T): # calculate oligo melting temp based on length
	if A + C + G + T <= 13: 
		Tm = (A+T)*2 + (G+C)*4                 # for short oligos
		return Tm
	else:
		Tm = 64.9 + 41*(G+C-16.4) / (A+T+G+C)  # for long oligos
		return Tm
		
print(oligo_melt(5, 7, 3, 4))