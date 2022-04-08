# H-Index

def solution(citations):
    answer = 0
    citations.sort()
    
    for h1 in range(1, len(citations) + 1):
        count = 0
        for h2 in citations:
            if h2 >= h1:
                count += 1
        if count >= h1:
            answer = h1
    
    return answer
