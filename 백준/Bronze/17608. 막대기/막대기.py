import sys

N = int(sys.stdin.readline().rstrip())
num_list = []

for i in range(N):
    h = int(sys.stdin.readline().rstrip())
    num_list.append(h)

count = 0
max_height = 0

for i in reversed(num_list):
    if i > max_height:
        count +=1
        max_height = i

sys.stdout.write(str(count)+"\n")