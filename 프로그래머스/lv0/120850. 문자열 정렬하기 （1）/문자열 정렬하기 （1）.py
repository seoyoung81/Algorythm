def solution(my_string):
    answer = []
    num_lst = [str(i) for i in range(0, 10)]
    for num in my_string:
        if num in num_lst:
            answer.append(int(num))
    answer.sort()
    return answer