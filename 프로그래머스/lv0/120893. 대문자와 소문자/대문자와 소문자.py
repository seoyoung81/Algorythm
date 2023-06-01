def solution(my_string):
    answer = ''
    for str in my_string:
        if str.isupper():
            answer += str.lower()
        elif str.islower():
            answer += str.upper()
    return answer