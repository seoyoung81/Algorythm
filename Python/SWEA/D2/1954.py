T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    snail = [[0] * N for _ in range(N)]

    cnt = 2
    snail[0][0] = 1
    i = j = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    k = 0

    while cnt != N * N + 1:
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:     # 범위 내에 있으면
            snail[ni][nj] = cnt
            i = ni
            j = nj
            cnt += 1
        else:
            k += 1
            if k >= 4:
                k = 0

    print(snail)