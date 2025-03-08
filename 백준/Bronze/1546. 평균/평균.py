N = int(input())
score = list(map(int,input().split()))
sum_score = 0
max_score = int(max(score))

for i in score:
    sum_score += int(i)/max_score*100

print(sum_score/N)