# 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    j = 10
    for i in arr:
        if i != j:
            answer.append(i)
        j = i
    
    return answer
