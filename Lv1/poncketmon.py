# 폰켓몬

def solution(nums):
    answer = 0
    
    poncketmon = set(nums)
    
    if len(poncketmon) < int(len(nums) / 2):
        answer = len(poncketmon)
    else:
        answer = int(len(nums) / 2)
    
    return answer
