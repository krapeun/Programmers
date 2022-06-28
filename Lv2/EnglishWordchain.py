# 영어 끝말잇기

def solution(n, words):    
    used = [words[0]]
    turn = 1
    
    for i in range(1, len(words)):
        if i % n == 0:
            turn += 1
            
        # Fail
        if words[i - 1][-1] != words[i][0]:
            return [i % n + 1, turn]
        elif words[i] in used:
            return [i % n + 1, turn]
        # Success
        else:
            used.append(words[i])
            
        # No Fail
        if i == len(words) - 1:
            return [0, 0]
