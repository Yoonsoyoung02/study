T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    N_list = list(map(int,input().split()))
    student = []
    for j in N_list:
        student.append(j//K)
    print(sum(student))