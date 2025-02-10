N = map(int, input().split())
print(sum(i**2 for i in N) % 10)