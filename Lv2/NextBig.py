# 다음 큰 숫자

def solution(n):
    answer = n + 1
    
    binN = bin(n)
    
    while True:
        binAnswer = bin(answer)
        if binN.count('1') == binAnswer.count('1'):
            break
        answer += 1
    
    return answer
