num = list(map(int, input().split()))
num_list=[1,1,2,2,2,8]

for i in range(len(num)):
    print(num_list[i]-num[i], end=' ')