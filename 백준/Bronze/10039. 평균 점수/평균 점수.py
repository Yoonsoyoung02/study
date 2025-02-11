num_list = []

for i in range(5):
    num = int(input())
    if num < 40 :
        num = 40
        num_list.append(num)
    else:
        num_list.append(num)
    
print(f'{sum(num_list)//5}')