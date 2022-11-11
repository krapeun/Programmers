# 42888 오픈 채팅방

def solution(record):
    answer = []
    
    uid = {}
    
    for user in record:
        if user.split(' ')[0] in 'EnterChange':
            uid[user.split(' ')[1]] = user.split(' ')[2]
    
    for user in record:
        if user.split(' ')[0] == 'Enter':
            answer.append(uid[user.split(' ')[1]] + '님이 들어왔습니다.')
        elif user.split(' ')[0] == 'Leave':
            answer.append(uid[user.split(' ')[1]] + '님이 나갔습니다.')
    
    return answer
