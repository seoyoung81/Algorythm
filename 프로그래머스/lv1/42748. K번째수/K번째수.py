def solution(array, commands):
    answer = []
    for lst in commands:
        lst2 = sorted(array[lst[0]-1:lst[1]])
        # print(lst2)
        answer.append(lst2[lst[2]-1])
    return answer