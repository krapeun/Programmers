# 체육복

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for reserve in reserve_set:
        if reserve - 1 in lost_set:
            lost_set.remove(reserve - 1)
        elif reserve + 1 in lost_set:
            lost_set.remove(reserve + 1)    
    
    return n - len(lost_set)
