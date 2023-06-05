def solution(num, k):
    answer = -1
    num_lst = list(str(num))
    for i in range(len(num_lst)):
        if num_lst[i] == str(k):
            answer = i + 1
            break
    
    return answer