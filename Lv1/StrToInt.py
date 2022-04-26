# 문자열을 정수로 바꾸기

def solution(s):
    answer = 0
    
    if s[0] == '-':
        s = s.split('-')[1]
        answer = -int(s)
    elif s[0] == '+':
        s = s.split('+')[1]
        answer = int(s)
    else:
        answer = int(s)
            
    return answer
