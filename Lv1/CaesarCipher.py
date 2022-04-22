# 시저 암호

def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(0, len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    
    answer = ''.join(s)
    
    return answer
