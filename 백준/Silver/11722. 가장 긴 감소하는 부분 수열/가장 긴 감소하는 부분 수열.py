n = int(input())
arr = list(map(int,input().split()))

def lis_memoization(arr):
    n = len(arr)
    dp = [-1] * n

    def lis_ending_at(i):
        if dp[i] != -1:
            return dp[i]

        dp[i] = 1
        
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], lis_ending_at(j) + 1)

        return dp[i]

    return max(lis_ending_at(i) for i in range(n))

print(lis_memoization(arr))