N = int(input()) 
con = str(input())

stack = []

for i in con :
    if 'a' <= i <= 'z':
        stack.append(i)
    else:
        if not stack or stack[-1] != i.lower():
            print(0)
            exit() 
        else:
            stack.pop()
print(1 if not stack else 0)