# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    
    if a < b:
        start = a
        fin = b + 1
    else:
        start = b
        fin = a + 1
    
    for i in range(start, fin):
        answer += i
    
    return answer
