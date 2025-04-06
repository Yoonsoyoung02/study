n1, n2 = map(int,input().split())

a = 100-n1
b = 100-n2
c=100-(a+b)
d = a*b
r=d%100
q=d//100

if len(str(d))>2:    
    print(a,b,c,d,q,r)
    print(c+q,r)  
else:
    print(a,b,c,d,q,r)
    print(c,d)