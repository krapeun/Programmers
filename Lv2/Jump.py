# 멀리 뛰기

def solution(n):
    jump = [0, 1, 2]
    for i in range(0, n + 1):
        if i > 2:
            jump.append(jump[i - 1] + jump[i - 2])
            
    return jump[n] % 1234567
