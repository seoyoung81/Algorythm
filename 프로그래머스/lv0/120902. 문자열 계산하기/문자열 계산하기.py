def solution(my_string):
    lst = list(my_string.split(' '))
    answer = int(lst[0])
    for i in range(len(lst)//2+1):
        if lst[i*2-1] == '+':
            answer += int(lst[i*2])
        elif lst[i*2-1] == '-':
            answer -= int(lst[i*2])
    return answer