def rank(num):
    if num < 2:
        rank = 6
    elif num == 2:
        rank = 5
    elif num == 3:
        rank = 4
    elif num == 4:
        rank = 3
    elif num == 5:
        rank = 2
    elif num == 6:
        rank = 1
        
    return rank

def solution(lottos, win_nums):
    answer = []
    
    zero_num = 0
    ans_min = 0
    ans_max = 0
    
    for i in lottos:
        if i == 0:
            zero_num += 1
        if i in win_nums:
            ans_min += 1
    
    ans_max = zero_num + ans_min
    
    answer.append(rank(ans_max))
    answer.append(rank(ans_min))
    
    return answer
