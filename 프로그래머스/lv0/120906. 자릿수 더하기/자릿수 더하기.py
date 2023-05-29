def solution(n):
    answer = 0
    num_lst = [int(i) for i in str(n)]
    for num in num_lst:
        answer += num
    return answer