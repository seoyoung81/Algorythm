def solution(num, total):
    answer = []
    a = total // num
    m = num // 2
    if total % num:
        answer = [i for i in range(a-m+1, a+m+1)]
    else:
        answer = [i for i in range(a-m, a+m+1)]
    return answer