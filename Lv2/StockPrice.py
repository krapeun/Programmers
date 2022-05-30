# 주식 가격

def solution(prices):
    answer = []
    
    for p in range(len(prices)):
        a = 0
        for i in range(p + 1, len(prices)):
            a += 1
            if prices[p] > prices[i]:
                break
        answer.append(a)
    
    return answer
