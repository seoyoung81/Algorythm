def solution(s):
    answer = 0
    lst = list(s.split(' '))
    print(lst)
    for i in range(len(lst)):
        if lst[i] == 'Z':
            answer -= int(lst[i-1])
        else:
            answer += int(lst[i])
    return answer