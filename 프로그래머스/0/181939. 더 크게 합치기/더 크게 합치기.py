def solution(a, b):
    num1 = str(a) + str(b)
    num2 = str(b) + str(a)
    return max(int(num1),int(num2))