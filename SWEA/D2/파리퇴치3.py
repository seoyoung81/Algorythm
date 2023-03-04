T = int(input())    # test case
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N X N arr , 스프레이 세기
    arr = [list(map(int, input().split())) for _ in range(N)] # 파리 개수 담은 2차원 리스트

    # 파리 퇴치
    ans = 0
    for start_i in range(N):
        for start_j in range(N):
            cnt = arr[start_i][start_j]
            # +
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):   # 상우하좌 탐색
                for mul in range(1, M):     # M 만큼 상우하좌 보기
                    next_i = start_i + di * mul
                    next_j = start_j + dj * mul
                    if 0 <= next_i < N and 0 <= next_j < N:     # 범위 내에 있는 경우만
                        cnt += arr[next_i][next_j]
            ans = max(ans, cnt)

            # x
            cnt = arr[start_i][start_j]
            for di, dj in ((-1, -1), (-1, 1), (1, 1), (1, -1)):     # 좌상 우상 우하 좌하 탐색
                for mul in range(1, M):
                    next_i = start_i + di * mul
                    next_j = start_j + dj * mul
                    if 0 <= next_i < N and 0 <= next_j < N:  # 범위 내에 있는 경우만
                        cnt += arr[next_i][next_j]
            ans = max(ans, cnt)


    print(f'#{test_case}', ans)