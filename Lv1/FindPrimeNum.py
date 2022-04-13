# 소수 찾기

import math

def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0 and i != 2:
                answer += 1
                break
                
    answer = n - answer - 1
    
    return answer
