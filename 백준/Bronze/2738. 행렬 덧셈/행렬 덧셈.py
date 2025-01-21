N,M = map(int,input().split())

A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

B = []
for _ in range(N):
    B.append(list(map(int,input().split())))

AB_sum= [[A[i][j] + B[i][j] for j in range (M)] for i in range(N)]

for i in AB_sum:
    print(' '.join(map(str,i)))