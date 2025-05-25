str = input()
answer = []
for i in str:
    if i == i.lower():
        i = i.upper()
        print(i, end='')
    else:
        i = i.lower()
        print(i, end='')

