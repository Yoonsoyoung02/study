N,M = map(int,input().split())
A= []
for i  in range(1,N+1):
    A.append(i)

for _ in range(M):
    i,j = map(int,input().split())
    A[i-1:j] = reversed(A[i-1:j])
print(*A)