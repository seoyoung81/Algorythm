def solution(a, b, n):
    answer = 0
    # a병주면 b병받음, 가지고 있는 빈병의 개수 n병
    while n >= a:
        answer += n // a * b
        n = n % a + n // a * b
    return answer