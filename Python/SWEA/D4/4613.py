T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N x M arr
    arr = [input() for _ in range(N)]   # 한 개의 행씩 문자열로 받기

    # 3개의 영역으로 나누기
    minV = N * M                # 칠해야 하는 개수의 최솟값(다 칠하는 경우에서 시작)
    for a in range(N-2):    # 첫번째 영역은 3개로 나눴을 때 N-3 까지 갈 수 있음 (W 영역 맨 아래)
        for b in range(a+1, N-1):   # 두번째 영역은 a+1 ~ N-2 까지  B
            # for c in range(b+1, N): # 마지막 영역은 b+1 ~ N-1 까지  R -> 굳이 안 정해도 됨
            cnt = 0                   # 각 영역에서 새로 칠하는 횟수
            for i in range(0, a+1):     # W 영역에서
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1

            for i in range(a+1, b+1):     # B 영역에서
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1

            for i in range(b+1, N):     # R 영역에서
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            minV = min(minV, cnt)
    print(f'#{test_case}', minV)