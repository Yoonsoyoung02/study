from collections import deque
del_list =[]

N = int(input())
queue = deque(range(1,N+1))

while len(queue)>1:
    del_list.append(queue.popleft())
    queue.append(queue.popleft())

print(queue[0])