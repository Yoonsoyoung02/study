# 정수의 개수 입력
N = int(input())

# 정수 목록 입력
numbers = list(map(int, input().split()))

# 찾으려는 정수 입력
v = int(input())

# 정수 v의 개수 세기
count = numbers.count(v)

# 결과 출력
print(count)
