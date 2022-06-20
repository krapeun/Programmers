# 피보나치 수

def solution(n):
    fibo = []
    
    for i in range(0, n + 1):
        if i == 0:
            fibo.append(0)
        elif i == 1 or i == 2:
            fibo.append(1)
        else:
            fibo.append(fibo[i - 2] + fibo[i - 1])
    
    return fibo[n] % 1234567
