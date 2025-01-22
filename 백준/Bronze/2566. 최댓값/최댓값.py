A = []
list_A=[]

for _ in range(9):
    A.append(list(map(int,input().split())))

for i, row in enumerate(A):
    for j, value in enumerate(row):
        list_A.append(value)
        if value == max(list_A):
            max_value = value
            max_i,max_j = i+1,j+1

print(max_value)
print(max_i,max_j)