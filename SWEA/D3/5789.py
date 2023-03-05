T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())    # N 개의 정수, Q 회 변경
    numbers = [0] * (N+1)
    for k in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            numbers[i] = k
    print(f'#{test_case}', *numbers[1:])