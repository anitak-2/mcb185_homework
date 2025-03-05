# 35scoringmatrix.py by Anita Kim
import sys

def generate_scoring_matrix(nuc, match_score, mismatch_score):
    letters = list(nuc)

    print("  ", end="")
    for letter in letters:
        print(letter, end=" ")
    print()

    for row in letters:
        print(row, end=" ")
        for col in letters:
            if row == col:
                print(match_score, end=" ")
            else:
                print(mismatch_score, end=" ")
        print()
        
nuc = sys.argv[1]
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])

generate_scoring_matrix(nuc, match_score, mismatch_score)