dollar_dic = { 
    'Franklin': 100, 
    'Grant':50, 
    'Jackson':20, 
    'Hamilton':10, 
    'Lincoln':5, 
    'Washington':1}

N = int(input())

for _ in range(N):
    name = input().split()
    dollar=[]
    for i in name:
        dollar.append(dollar_dic[i])
    print(f'${sum(dollar)}')