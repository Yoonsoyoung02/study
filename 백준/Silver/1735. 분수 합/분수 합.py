import math

A1,B1 = map(int,input().split())
A2,B2 = map(int,input().split())

B3 = math.lcm(B1,B2)
A3 = A1*(B3//B1)+A2*(B3//B2)

gcd=math.gcd(A3,B3)

A3 = A3//gcd
B3 = B3//gcd

print(A3,B3)