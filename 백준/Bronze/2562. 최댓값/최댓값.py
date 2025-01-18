A = []
for i in range(9):
    A.append(int(input()))
max_value = A[0]
max_idx = 0

for idx, value in enumerate(A):
    if value > max_value:
        max_value = value
        max_idx = idx

print(max_value)
print(max_idx+1)