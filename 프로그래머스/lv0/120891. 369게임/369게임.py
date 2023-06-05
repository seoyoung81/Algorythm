def solution(order):
    answer = 0
    order = list(str(order))
    for num in order:
        if num in ['3', '6', '9']:
            answer += 1
    return answer