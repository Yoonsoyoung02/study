def solution(myString, pat):
    answer = 0
    lower_pat = pat.lower()
    lower_myString = myString.lower()
    
    if lower_pat in lower_myString:
        answer=1
    else:
        answer=0
    return answer