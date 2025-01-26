A = int(input())
result = []


result = [[0] * 100 for _ in range(100)]

for i in range(A):
    N,M = map(int,input().split())
    for i in range (N,N+10):
        for j in range(M,M+10):
                result[i][j] = 1

total_sum = 0

for row in result:
    for value in row:
        total_sum += value

print(total_sum)