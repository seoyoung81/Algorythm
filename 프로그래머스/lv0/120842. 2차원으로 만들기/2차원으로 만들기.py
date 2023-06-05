def solution(num_list, n):
    answer = []
    m = len(num_list) // n
    for i in range(m):
        answer.append([])
    
    for num in num_list:
        for i in range(m):
            if len(answer[i]) != n:
                answer[i].append(num)
                break
    return answer