# 76502 괄호 회전하기

def solution(s):
    answer = 0
    
    # 괄호 회전
    for i in range(len(s)):
        rotates = list(s[i:len(s)] + s[0:i])
        stack = []
        
        for rotate in rotates:
            if len(stack) != 0:
                if stack[-1] == '(' and rotate == ')':
                    stack.pop()
                elif stack[-1] == '[' and rotate == ']':
                    stack.pop()
                elif stack[-1] == '{' and rotate == '}':
                    stack.pop()
                else:
                    stack.append(rotate)
            else:
                stack.append(rotate)
                
        # 모두 짝이 맞은 경우
        if len(stack) == 0:
            answer += 1
        
    return answer
