# 예산

def solution(d, budget):
    answer = 0
    
    d.sort()
    
    while sum(d) > budget:
        d.pop()
        
    answer = len(d)
    
    return answer
