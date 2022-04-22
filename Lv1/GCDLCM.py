# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
          
    k = max(n, m)
    while True:
        if k % n == 0 and k % m == 0:
            answer.append(k)
            break
        k += max(n, m)
    
    return answer
