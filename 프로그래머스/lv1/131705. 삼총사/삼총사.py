def solution(number):
    answer = 0
    m = len(number)
    for i in range(m):
        for j in range(i+1, m):
            for k in range(j+1, m):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer