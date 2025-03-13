num_list = []

for i in range (10):
    num = int(input())
    num_list.append(num % 42)
s_num_list = sorted(num_list)

cnt= 0
previous_num = s_num_list[0]

for j in s_num_list:
    if j != previous_num:
        cnt+=1
        previous_num = j
print(cnt+1)
