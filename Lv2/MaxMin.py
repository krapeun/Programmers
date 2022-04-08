# 최댓값과 최솟값

def solution(s):
    answer = ''
    
    number = list(map(int, s.split(' ')))
    number.sort()
    
    answer += str(number[0])
    answer += ' '
    answer += str(number[len(number) - 1])
    
    return answer
