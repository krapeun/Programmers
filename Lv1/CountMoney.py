# 부족한 금액 계산하기

def solution(price, money, count):
    answer = 0
    
    priceN = 0
    for i in range(1, count + 1):
        priceN += price * i
        
    if priceN - money > 0:
        answer = priceN - money

    return answer
