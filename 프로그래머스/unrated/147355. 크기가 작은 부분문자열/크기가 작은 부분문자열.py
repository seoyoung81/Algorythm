def solution(t, p):
    answer = 0
    m = len(p)
    n = len(t)
    for i in range(n-m+1):
        if int(t[i:i+m]) <= int(p):
            answer += 1
    return answer