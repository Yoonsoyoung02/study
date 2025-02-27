import sys
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

T = int(sys.stdin.readline().strip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A, B))
