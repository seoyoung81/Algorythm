def solution(num_list):
    answer = []
    m = len(num_list)
    for i in range(m-1, -1, -1):
        answer.append(num_list[i])
    return answer