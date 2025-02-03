import sys

N = int(sys.stdin.readline().strip())
num_list=[]

for i in range(N):
    com = list(map(int, sys.stdin.readline().split()))

    if com[0] == 1:
        num_list.append(com[1])

    elif com[0] == 5:
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[-1])

    elif com[0] == 3 :
        print(len(num_list))

    elif com[0] == 2:
        print(num_list.pop() if num_list else -1)

    elif com[0] == 4:
        print(1 if not num_list else 0)