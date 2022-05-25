# 신규 아이디 추천

def solution(new_id):
    answer = ''
    
    # lv1
    new_id = new_id.lower()
    
    # lv2
    id_list = ['-', '_', '.']
    
    for ID in new_id:
        if 'a' <= ID <= 'z':
            answer += ID
        elif '0' <= ID <= '9':
            answer += ID
        elif ID in id_list:
            answer += ID
            
    # lv3
    while '..' in answer:
        answer = answer.replace('..', '.')
            
    # lv4
    if answer[0] == '.':
        answer = answer[- (len(answer) - 1):]
    if answer[-1] == '.':
        answer = answer[:len(answer) - 1]
    
    # lv5
    if len(answer) == 0:
        answer += 'a'
        
    # lv6
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:len(answer) - 1]
        
    # lv7
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer
