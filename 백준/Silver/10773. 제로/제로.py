K = int(input())
num_list = []

for i in range (K):
    num = int(input())
    if num == 0:
        num_list.pop(-1)
    else:
        num_list.append(num)

print(sum(num_list))