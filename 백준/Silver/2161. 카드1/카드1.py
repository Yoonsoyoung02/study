from collections import deque

N = int(input())
queue = deque(range(1, N+1))
del_list = []

while len(queue) > 1:
    del_list.append(queue.popleft()) 
    queue.append(queue.popleft())


print(*del_list, queue[0]) 