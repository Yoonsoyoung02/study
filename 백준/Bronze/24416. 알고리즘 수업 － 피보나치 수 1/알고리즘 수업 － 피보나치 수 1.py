import sys

def fib(n, memo):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1 
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

def fibonacci(n):
    return n - 2 

n = int(sys.stdin.readline().strip())

recursive_count = fib(n, {})

dp_count = fibonacci(n)
print(recursive_count, dp_count)
