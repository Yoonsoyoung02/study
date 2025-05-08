A, B = input().split()

rev_A = A[::-1]
rev_B = B[::-1]

print(max(int(rev_A), int(rev_B)))
