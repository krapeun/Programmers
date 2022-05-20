# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = [''] * n
    
    dec1 = []
    dec2 = []
    
    for i in range(n):
        str1 = []
        str2 = []
        for j in range(len(arr1)):
            str1.append(str(arr1[i] % 2))
            str2.append(str(arr2[i] % 2))
            arr1[i] = int(arr1[i] / 2)
            arr2[i] = int(arr2[i] / 2)

        str1.reverse()
        str2.reverse()
        dec1.append(''.join(str1))
        dec2.append(''.join(str2))

    for i in range(n):
        for j in range(n):
            if dec1[i][j] == '0' and dec2[i][j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    
    return answer
