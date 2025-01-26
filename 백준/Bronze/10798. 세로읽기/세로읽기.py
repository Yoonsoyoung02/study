A = []
result = []

for _ in range (5):  # [0,0,0,0,0]
    A.append(input())


max_len = 0

for line in A:
    if max_len < len(line):
        max_len = len(line)

for i in range (max_len):
    for j in range(5):
        if i < len(A[j]):
            result.append(A[j][i])

print(''.join(result))