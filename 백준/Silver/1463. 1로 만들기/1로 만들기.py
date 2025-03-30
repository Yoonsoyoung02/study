N = int(input())
dp = [0]*(N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1]+1 # 미리 한 번 빼본 값, 앞의 횟수 계산 결과에서 1 더한 값과 추후 먼저 나눈 값을 비교
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[N])