# 이상한 문자 만들기

def solution(s):
    answer = ''
    
    s = list(s.split(' '))
    
    for word in s:
        for i in range(0, len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '

    answer = ' '.join(answer.split(' ')[0:-1])
    return answer
