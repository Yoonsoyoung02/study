import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    num = list(map(int,sys.stdin.readline().rstrip().split()))
    a,b = num[0],num[1]

    while b > 0:
        a,b = b,a%b

    sys.stdout.write(str(a)+'\n')