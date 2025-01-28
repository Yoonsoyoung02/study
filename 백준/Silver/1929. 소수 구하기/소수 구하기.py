import sys

def find_prime(M, N):
    num = [True] * (N + 1)
    num[0], num[1] = False, False

    for i in range(2, int(N**0.5) + 1):
        if num[i]:
            for j in range(i * i, N + 1, i):
                num[j] = False

    print('\n'.join(str(i) for i in range(M, N + 1) if num[i]))

M, N = map(int, sys.stdin.read().split())
find_prime(M, N)