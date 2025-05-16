string = input()

num = 0

for i in range(len(string)//2):
    if string[i] == string[len(string)-i-1]:
        num +=1

if num == len(string)//2:
    print(1)
else:
    print(0)