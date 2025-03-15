def solution(numbers):
    answer = ''
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x * 10, reverse=True)

    if numbers_str[0] == '0':
        answer = '0';
    else:
        answer = ''.join(numbers_str)
    return answer