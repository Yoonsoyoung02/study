N = int(input())

for i in range(N):
    R,S = input().split()
    N_list=[]
    for i in S:
        N_list.append(i*int(R))
    print("".join(N_list))