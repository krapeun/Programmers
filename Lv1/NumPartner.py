# 숫자 짝꿍

def solution(X, Y):
    answer = []
    
    # 자리수마다 초기화 (0~9)
    Xs = [0] * 10
    Ys = [0] * 10
    
    for x in X:
        Xs[int(x)] += 1
    for y in Y:
        Ys[int(y)] += 1
    
    # X, Y 비교하여 짝지을 수 있는 만큼 answer에 추가
    for i in range(10):
        if Xs[i] > 0 and Ys[i] > 0:
            for j in range(min(Xs[i], Ys[i])):
                answer.append(i)

    # 예외 처리
    if len(answer) == 0:
        return "-1"
    elif answer[-1] == 0:
        return "0"
    
    # 가장 큰 정수
    answer.sort(reverse = True)
    answer = list(map(str, answer))
    answer = "".join(answer)
    
    return answer
