N = int(input())

for i in range(N):
    score = list(input())
    plus = 0 
    total = 0
    for j in score:
        if j =='O':
            plus +=1
            total +=plus
        else:
            plus = 0
    print(total)