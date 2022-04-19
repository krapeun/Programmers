# 정수 제곱근 판별

def solution(n):
    answer = -1
    
    x = int(n ** (1/2))
    if x * x == n:
        answer = (x + 1) * (x + 1)
    
    return answer
