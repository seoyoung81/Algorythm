T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N 줄에 M 개씩

    arr = [list(map(int, input().split())) for _ in range(N)]   # 풍선 정보 입력받기

    result = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):   # 상우하좌
                A = arr[i][j]
                for mul in range(1, A+1):
                    ni = i + di * mul
                    nj = j + dj * mul
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            # print(cnt)
            result = max(cnt, result)
    print(f'#{test_case}', result)