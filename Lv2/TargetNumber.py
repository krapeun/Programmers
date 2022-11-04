# 43165 타겟 넘버

def solution(numbers, target):
    results = [0]
    
    for num in numbers:
        nextarr = []
        # 다음 연산 수행
        for result in results:
            nextarr.append(result + num)
            nextarr.append(result - num)
        results = nextarr
    
    # 전체 결과 중 타겟 넘버의 개수
    answer = results.count(target)
        
    return answer
