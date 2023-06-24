def solution(phone_number):
    answer = ''
    m = len(phone_number)
    answer += '*' * (m-4)
    answer += phone_number[m-4:]
    return answer