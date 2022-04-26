# 두 개 뽑아서 더하기

import itertools

def solution(numbers):
    answer = []
    
    com = list(itertools.combinations(numbers, 2))
    sumlist = list(map(sum, com))
    sumlist.sort()
    
    for i in sumlist:
        if i not in answer:
            answer.append(i)
    
    return answer
