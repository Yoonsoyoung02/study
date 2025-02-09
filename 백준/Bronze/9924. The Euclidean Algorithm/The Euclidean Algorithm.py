import sys

def gcd(a, b):
    count = 0
    while a != b:
        count += 1
        a, b = max(a, b) - min(a, b), min(a, b)
    return count

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(f'{gcd(a, b)}\n')