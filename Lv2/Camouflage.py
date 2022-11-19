# 42578 위장

def solution(clothes):
    answer = 1
    
    clothes_count = {}
    for c, type in clothes:
        clothes_count[type] = clothes_count.get(type, 0) + 1

    for type in clothes_count:
        answer *= (clothes_count[type] + 1)
    
    return answer - 1
