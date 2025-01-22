N = int(input())


for i in range(N):
    sum_A = 0
    list_A = []
    A = list(map(int,input().split()))
    for j in A:
        if j % 2 == 0:
            sum_A += j
            list_A.append(j)
    print(sum_A,min(list_A))