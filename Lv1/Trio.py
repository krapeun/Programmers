# 삼총사

import itertools

def solution(number):
    answer = 0
    
    trios = list(itertools.combinations(number, 3))

    for trio in trios:
        if sum(trio) == 0:
            answer += 1
    
    return answer
