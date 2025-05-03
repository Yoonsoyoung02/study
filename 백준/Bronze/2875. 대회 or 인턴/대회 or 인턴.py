def max_teams(N, M, K):
    max_team = min(N // 2, M)

    while max_team > 0:
        if N + M - (max_team * 3) >= K:
            return max_team
        max_team -= 1

    return 0

N, M, K = map(int, input().split())
print(max_teams(N, M, K))
