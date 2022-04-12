# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    
    for i in range(0, len(phone_number)):
        if i >= len(phone_number) - 4:
            answer += phone_number[i]
        else:
            answer += '*'
    
    return answer
