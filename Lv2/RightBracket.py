# 12909 올바른 괄호

def solution(s):
    answer = True
    
    stack = []
    
    for string in s:
        if string == ')':
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
        else:
            stack.append(string)
            
    if len(stack) != 0:
        answer = False

    return answer
