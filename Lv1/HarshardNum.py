# 하샤드 수

def solution(x):
    answer = False
    
    newX = str(x)
    sumX = 0
    for i in newX:
        sumX += int(i)
    
    if x % sumX == 0:
        answer = True
    
    return answer
