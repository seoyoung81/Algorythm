def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        answer[i] = numbers[i] * 2
    return answer