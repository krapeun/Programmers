# 2016년

def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    date = b
    for i in range(a - 1):
        date += month[i]
    
    return day[date % 7]
