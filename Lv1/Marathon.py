# 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    answer = ''
    
    par = Counter(participant)
    com = Counter(completion)
    
    par.subtract(com)

    answer += sorted(par.elements())[0]
    
    return answer
