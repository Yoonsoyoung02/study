N = int(input())

for i in range(N):
    vps = input()
    count = 0

    for j in vps:
        if j == '(':
            count +=1
        elif j == ')':
            count -=1
        if count < 0:
            break
    
    if count == 0 :
        print('YES')
    else:
        print('NO')