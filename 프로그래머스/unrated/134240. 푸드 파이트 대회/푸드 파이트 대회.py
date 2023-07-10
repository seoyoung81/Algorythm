def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] == 1:
            pass
        else:
            answer += (food[i] // 2) * str(i)
    m = len(answer)
    answer += '0'
    answer += answer[m-1::-1]
    return answer