def fibonacci():

    dp = [[0,0] for _ in range(41)] # 최대값 40 -> [0,0] 초기화

    # 피보나치 수열과 마찬가지로 1,2 번째 값 초기화
    dp[0] = [1,0] # [0의 개수, 1의 개수]
    dp[1] = [0,1]

    for i in range(2,41):
        dp[i][0] = dp[i-2][0]+dp[i-1][0]
        dp[i][1] = dp[i-2][1]+dp[i-1][1]

    T = int(input())

    for _ in range(T):
        n = int(input())

        print(dp[n][0],dp[n][1])

fibonacci()