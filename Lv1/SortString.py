# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    
    strings = sorted(strings)
    answer = sorted(strings, key = lambda x:x[n])
    
    return answer
