# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a:
            return answer
        
        x = n % a
        bottle = int(n / a) * b
        n = bottle + x
        answer += bottle
