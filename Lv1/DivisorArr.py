# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    count = 0
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            count += 1
    
    if count == 0:
        answer.append(-1)
    
    answer.sort()
    
    return answer
