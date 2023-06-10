def solution(my_string):
    answer = 0
    my_string= list(my_string)
    i = 0
    num = ''
    while i != len(my_string):    
        if not my_string[i].isalpha():
            num += my_string[i]
        else:
            if num:
                answer += int(num)
                num = ''
        i += 1
    if num:
        answer += int(num)
    return answer