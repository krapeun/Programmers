# 3진법 뒤집기

import math

def solution(n):
    answer = 0

    n3 = []
    
    while True:
        if n == 0:
            break
        n3.append(n % 3)
        n = int(n / 3)
        
    n3.reverse()
    
    for i in range(len(n3)):
        answer += n3[i] * (pow(3, i))
    
    return answer
