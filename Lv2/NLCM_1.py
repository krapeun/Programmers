# N개의 최소공배수
# 반복문 사용 -> 나중에 수정

def solution(arr):
    idx = 1
    arr.sort()

    while True:
        arrMax = arr[-1] * idx
        for i in arr:
            if arrMax % i != 0:
                idx += 1
                break
            if i == arr[-1]:
                return arrMax
