num = int(input())

for i in range(num):
    A,B,X = map(int,input().split())
    print(A*(X-1)+B)