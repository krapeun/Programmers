# 점프와 순간 이동

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            ans += 1
            n -= 1
            n /= 2

    return ans
