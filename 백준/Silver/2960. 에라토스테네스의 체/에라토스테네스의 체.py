N,K = map(int, input().split())
numbers = [True]*(N+1)
numbers[0]= False
numbers[1] = False

count = 0

for i in range(2,N+1):
    if numbers[i]:
        for j in range(i,N+1,i):
            if numbers[j]:
                numbers[j] = False
                count +=1
                if count == K:
                    print(j)