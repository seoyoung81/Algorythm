T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N x N arr, 스프레이 세기 M
    arr = [list(map(int, input().split())) for _ in range(N)]   # 파리 정보 입력 받기

    # + 모양으로 잡기
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):   # 상우하좌
                for mul in range(1, M):    # 세기 M
                    ni = i + di * mul
                    nj = j + dj * mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            # print(cnt)
            result = max(result, cnt)

    # X 모양으로 잡기
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for di, dj in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
                for mul in range(1, M):    # 세기 M
                    ni = i + di * mul
                    nj = j + dj * mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            result = max(result, cnt)

    print(f'#{test_case}', result)