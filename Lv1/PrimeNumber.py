# 소수 만들기

import itertools

def solution(nums):
    answer = 0

    # 3개의 숫자 조합
    combi = itertools.combinations(nums, 3)
    combi_sum = []
    for i in combi:
        combi_sum.append(sum(i))
    
    for i in combi_sum:
        divisor = 0
        # 제곱근까지 떨어지는 숫자가 있는지 확인
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                divisor += 1
                break
        if divisor == 0:
            answer += 1

    return answer
