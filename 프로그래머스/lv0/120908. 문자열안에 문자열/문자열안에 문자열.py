def solution(str1, str2):
    answer = 2
    m = len(str2)
    n = len(str1)
    for i in range(n-m+1):
        if str1[i:i+m] == str2:
            answer = 1
    return answer