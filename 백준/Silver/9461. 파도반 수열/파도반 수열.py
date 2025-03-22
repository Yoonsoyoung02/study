def fibonacci(n,memo=None):
    if memo is None:
        memo = [-1]*(n+1)
    
    if n <=1: # 0,1은 원래 값으로 반환 
        return n
    elif n==2:
        return 1
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci(n-3,memo) + fibonacci(n-2,memo)

    return memo[n]

N = int(input())
for i in range(N):
    T = int(input())
    print(fibonacci(T))