from collections import deque

N,K = map(int,input().split())
num_list = deque([i for i in range(1,N+1)])
del_list=[]

while len(num_list) != 0:
    for i in range(K-1):
        num_list.append(num_list.popleft())
    del_list.append(str(num_list.popleft()))

print('<'+', '.join(del_list)+'>')