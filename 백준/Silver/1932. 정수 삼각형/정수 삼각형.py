N = int(input())

triangle = [list(map(int,input().split())) for _ in range(N)]

for i in range(N-2,-1,-1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])