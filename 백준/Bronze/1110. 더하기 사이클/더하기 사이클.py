N = int(input())
N_origin = N
cnt = 0

while True:
    cnt +=1

    a = N%10   
    b = N//10 
    c = (a+b)%10 
    N = a*10 + c

    if N == N_origin:
        break
print(cnt)