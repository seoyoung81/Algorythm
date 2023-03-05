T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N X M 격자판
    arr = [list(map(int, input().split())) for _ in range(N)]   # 풍선 정보 입력 받기

    result = 0
    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    flower += arr[ni][nj]
            result = max(result, flower)

    print(f'#{test_case}', result)