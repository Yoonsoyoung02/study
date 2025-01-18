N,M = map(int,input().split())
list =[0]*N

for _ in range(M):
    i,j,k=map(int,input().split())
    if 1 <= i <= j <= N and 1 <= k <= N:
        for a in range(i-1,j):
            list[a] = k
print(*list)