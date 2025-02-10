N = map(int,input().split())
num_list = []
for i in N:
    num_list.append(i**2)
print(sum(num_list)%10)