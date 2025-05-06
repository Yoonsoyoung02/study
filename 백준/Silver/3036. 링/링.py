import math
N = int(input())

N_list = list(map(int, input().split()))

for i in N_list[1:]:
    gcd = math.gcd(N_list[0], i)
    print(f'{N_list[0]//gcd}/{i//gcd}')