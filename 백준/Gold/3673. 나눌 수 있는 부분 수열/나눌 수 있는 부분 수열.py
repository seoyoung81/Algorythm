import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    # 연속하는 부분 수열의 합이 d로 나누어 떠어지는 것의 개
    d, n = map(int, input().split())
    number = [0] + list(map(int, input().split()))
    result = 0
    number_sum = [0] * (n+1)
    number_mod = [0] * (n+1)
    for i in range(1, n+1):
        number_sum[i] = number_sum[i-1] + number[i]
        if number_sum[i] % d == 0:
            result += 1
        number_mod[i] = number_sum[i] % d

    # number_sum의 숫자들에서 d로 나눈 나머지의 값이 같은 값인 경우 -> 나누어 떨어진다
    mod_count = [0] * (d+1)
    mod_count[0] = -1
    for num in number_mod:
        mod_count[num] += 1

    for num in mod_count:
        result += num * (num-1) // 2

    print(result)


