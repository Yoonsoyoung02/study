def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_primes(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_palindrom_prime(num): 
    N = num
    while True: #만족하는 N이 나오면 바로 출력 되도록
        if is_primes(num) and is_palindrome(num):
            return num
        num +=1

N = int(input())

print(find_palindrom_prime(N))