# 숫자 문자열과 영단어

def solution(s):
    answer = ''
    
    eng = ''
    isNum = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for word in s:
        if '0' <= word <= '9':
            answer += word
        else:
            eng += word
        if eng in isNum:
            answer += str(isNum.index(eng))
            eng = ''
    
    answer = int(answer)
    return answer
