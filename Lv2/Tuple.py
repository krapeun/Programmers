# 튜플

def solution(s):
    answer = []
    
    # Split String
    s_set = list(s.split('{{')[1].split('}}')[0].split('},{'))
    s_set = sorted(s_set, key = lambda x:len(x))
    
    # Split to Tuple
    new_set = []
    for s in s_set:
        new_set.append(list(s.split(',')))
    
    for new in new_set:
        # Str to Int
        new = map(int, new)
        for i in new:
            if i not in answer:
                answer.append(int(i))
    
    return answer
