T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    arr = [list(map(str, input().split())) for _ in range(N)]   # 2d arr

    # 270 도
    third_arr = [[0] * N for _ in range(N)]
    # 180 도
    second_arr = [[0] * N for _ in range(N)]
    # 90 도
    first_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            third_arr[N-1-j][i] = arr[i][j]
            first_arr[j][N-i-1] = arr[i][j]
            second_arr[N-i-1][N-j-1] = arr[i][j]

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(first_arr[i]), ''.join(second_arr[i]), ''.join(third_arr[i]))

