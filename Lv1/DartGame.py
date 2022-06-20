# [1차] 다트 게임

import math

def solution(dartResult):
    answer = 0
    
    dartResult = dartResult.replace('10', 'A')
    stack = []
    bonus = ['S', 'D', 'T']
    
    for dart in dartResult:
        if '0' <= dart <= '9' or dart == 'A':
            if dart == 'A':
                dart = '10'
            stack.append(int(dart))
        elif dart == '*':
            stack[-1] = stack[-1] * 2
            if len(stack) > 1:
                stack[-2] = stack[-2] * 2
        elif dart == '#':
            stack[-1] = - stack[-1]
        else:
            stack[-1] = pow(stack[-1], bonus.index(dart) + 1)
    
    while len(stack) != 0:
        answer += int(stack.pop())
    
    return answer
