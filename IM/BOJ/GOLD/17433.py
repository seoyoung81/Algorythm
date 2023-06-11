# 유클리드 호제법을 사용해서 최대공약수 구하기
def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # 각 숫자들의 차를 구하고 이 '차'의 최대공약수를 구하면 된다력
    # 두 수의 차가 m의 배수인 경우 -> 두 수를 m으로 각각 나누면 나머지가 같
    # 12, 14 -> 차가 2 -> 나머지 0
    # 23, 34 -> 차가 11 -> 나머지 1
    # a % m = x ... 1, b % m = x ...1 -> (a-b) % m = 0
    # 차가 모두 0인 경우 -> 숫자가 모두 같은 경우 무한 출

    diff = []
    for i in range(1, N):
        if arr[i] - arr[i-1] not in diff:
            diff.append(arr[i]-arr[i-1])

    if diff == [0]:
        print('INFINITY')
    else:
        x = diff[0]
        for i in range(1, len(diff)):
            temp = GCD(x, diff[i])
            x = temp
        print(x)

