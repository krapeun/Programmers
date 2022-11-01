# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    
    start = False
    
    for i, ss in enumerate(s):
        if ss == ' ':
            answer += ss
            start = True
        elif start == True or i == 0:
            answer += ss.upper()
            start = False
        else:
            answer += ss.lower()
            start = False
            
    return answer
