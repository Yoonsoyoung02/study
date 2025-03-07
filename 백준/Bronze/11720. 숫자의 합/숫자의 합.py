N = int(input())
num_list = input()

total_sum = 0
for idx,value in enumerate(num_list):
    total_sum += int(value)

print(total_sum)