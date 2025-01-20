import sys

# 테스트케이스 수 입력
T = int(sys.stdin.readline().rstrip())

# 결과 저장 리스트
results = []

# 테스트케이스 처리
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    results.append(A + B)

# 한 번에 출력
sys.stdout.write('\n'.join(map(str, results)) + '\n')
