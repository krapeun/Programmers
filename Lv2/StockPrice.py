# 주식 가격

def solution(prices):
    answer = []
    
    for p in range(len(prices)):
        a = 0
        for i in range(p + 1, len(prices)):
            if prices[p] <= prices[i]:
                a += 1
            else:
                a += 1
                break
        answer.append(a)
    
    return answer
