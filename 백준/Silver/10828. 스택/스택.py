import sys

N = int(sys.stdin.readline().strip())
num_list=[]

for i in range(N):
    com = sys.stdin.readline().strip()

    if 'push' in com:
        num_list.append(com[5:])

    elif com == 'top':
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[-1])

    elif com == 'size':
        print(len(num_list))

    elif com == 'pop':
        print(num_list.pop() if num_list else -1)

    elif com == 'empty':
        print(1 if not num_list else 0)