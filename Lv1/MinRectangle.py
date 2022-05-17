# 최소 직사각형

def solution(sizes):
    answer = 1
    
    x = 0
    y = 0
    
    for i in range(len(sizes)):
        sizes[i].sort()
        if x < sizes[i][0]:
            x = sizes[i][0]
        if y < sizes[i][1]:
            y = sizes[i][1]
    
    answer = x * y
    
    return answer
