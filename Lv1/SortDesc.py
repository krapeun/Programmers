# 정수 내림차순으로 배치하기

def solution(n):
    answer = ''
    
    newN = list(str(n))
    newN.sort(reverse = True)
    answer = ''.join(newN)
    
    return int(answer)
