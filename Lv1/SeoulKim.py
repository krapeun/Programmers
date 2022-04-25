# 서울에서 김서방 찾기

def solution(seoul):
    for i in range(0, len(seoul)):
        if seoul[i] == 'Kim':
            return '김서방은 ' + str(i) + '에 있다'
            break
