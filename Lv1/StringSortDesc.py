# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    string = list(s)
    string.sort(reverse = True)

    answer = "".join(string)
    return answer
