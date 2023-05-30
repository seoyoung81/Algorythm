def solution(my_string):
    answer = 0
    numbers = [str(i) for i in range(1, 11)]
    for string in my_string:
        if string in numbers:
            answer += int(string)
    return answer