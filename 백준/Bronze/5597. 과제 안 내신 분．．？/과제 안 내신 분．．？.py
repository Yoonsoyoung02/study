num_list = [i for i in range(1,31)]

for _ in range(28):
    n = int(input())
    if n in num_list:
        num_list.remove(n)
print(num_list[0])
print(num_list[1])
