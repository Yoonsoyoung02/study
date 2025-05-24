def solution(strArr):
    answer = []
    for idx,value in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(value.lower())
        else:
            answer.append(value.upper())
    return answer