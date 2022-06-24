# 모의고사

def solution(answers):
    answer = []
    correct = [0, 0, 0]
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(0, len(answers)):
        i1 = i % 5
        i2 = i % 8
        i3 = i % 10
        
        if answers[i] == s1[i1]:
            correct[0] += 1
        if answers[i] == s2[i2]:
            correct[1] += 1
        if answers[i] == s3[i3]:
            correct[2] += 1
            
    for i in range(0, len(correct)):
        if correct[i] == max(correct[0], correct[1], correct[2]):
            answer.append(i + 1)
    
    return answer
