T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N x N
    farm = [list(map(int, input())) for _ in range(N)]  # 2d arr

    total = 0
    M = N // 2

    for i in range(N):
        total += sum(farm[i][abs(M-i):N-abs(M-i)])

    print(f'#{test_case}', total)