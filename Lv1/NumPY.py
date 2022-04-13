# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    
    sumP = 0
    sumY = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            sumP += 1
        elif i == 'y' or i == 'Y':
            sumY += 1

    if sumP != sumY:
        answer = False
            
    return answer
