N = int(input())
num = 0 

for i in range(N):
    string = input()
    prev = ''
    used = set()
    is_group = True

    for j in string:
        if j !=prev:
            if j in used:
                is_group = False
                break
            used.add(j)
        prev = j
    if is_group:
        num +=1
print(num)