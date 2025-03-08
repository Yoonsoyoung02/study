import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
que_list = deque([])

for _ in range(N):
    com = sys.stdin.readline().rstrip().split()

    if com[0] == 'push':
        que_list.append(int(com[1]))

    elif com[0] == 'pop':
        if not que_list:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(que_list.popleft()) + '\n')

    elif com[0] == 'front':
        if not que_list:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(que_list[0]) + '\n')

    elif com[0] == 'size':
        sys.stdout.write(str(len(que_list)) + '\n')

    elif com[0] == 'empty':
        sys.stdout.write("1\n" if not que_list else "0\n")

    elif com[0] == 'back':
        if not que_list:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(que_list[-1]) + '\n')
