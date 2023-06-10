def solution(i, j, k):
    answer = 0
    for p in range(i, j+1):
        p = str(p)
        for num in p:
            if num == str(k):
                answer += 1
    return answer