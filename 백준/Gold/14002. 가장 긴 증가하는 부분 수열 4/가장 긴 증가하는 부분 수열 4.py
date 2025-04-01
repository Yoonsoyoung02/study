def LIS(N, arr):

    dp = [1] * N
    lis = [[arr[i]] for i in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                lis[i] = lis[j] + [arr[i]]
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    longest_list = lis[max_index]
    
    return max_length, longest_list

N = int(input())
arr = list(map(int, input().split()))

length, sequence = LIS(N, arr)

print(length)
print(*sequence)
