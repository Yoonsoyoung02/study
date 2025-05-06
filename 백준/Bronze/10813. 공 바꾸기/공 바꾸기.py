N,M= map(int, input().split())
N = [i for i in range(1,N+1)]

for i in range(M):
    a,b = map(int, input().split())
    N[a-1],N[b-1] = N[b-1],N[a-1]

print(*N)