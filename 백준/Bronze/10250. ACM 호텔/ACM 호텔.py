def assign_rooms_alternative(T, test_cases):
    results = []
    for H, W, N in test_cases:
        # 층수 계산 (N번째 손님이 몇 층에 배정될지)
        floor = (N - 1) % H + 1
        
        # 호실 계산 (손님 번호를 H로 나눈 몫을 사용)
        room = (N - 1) // H + 1
        
        # 결과 저장 (호실 번호를 두 자리로 맞춤)
        results.append(f"{floor}{room:02d}")
    
    return results

# 입력 받기
T = int(input())  # 테스트 케이스 개수
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# 결과 출력
for result in assign_rooms_alternative(T, test_cases):
    print(result)
