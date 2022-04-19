# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int, reversed(list(str(n)))))

    return answer
