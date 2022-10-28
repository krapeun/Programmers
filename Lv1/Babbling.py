# 133499 옹알이 (2)

def solution(babbling):
    answer = 0
    
    for bab in babbling:
        bab = bab.replace('aya', '1')
        bab = bab.replace('ye', '2')
        bab = bab.replace('woo', '3')
        bab = bab.replace('ma', '4')

        for i in range(len(bab)):
            if bab[i] > '4':
                break
            elif i > 0 and bab[i] == bab[i-1]:
                break
            if i == len(bab) - 1:
                answer += 1    
    
    return answer
