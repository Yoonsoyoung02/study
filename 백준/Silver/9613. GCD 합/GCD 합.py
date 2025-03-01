import math
t = int(input())

for _ in range(t):
    n = list(map(int,input().split()))
    num=n[0]
    numbers=n[1:]
    result=0
    
    for i in range(num):
        for j in range(i+1,num):
            result += math.gcd(numbers[i], numbers[j])
    print(result)