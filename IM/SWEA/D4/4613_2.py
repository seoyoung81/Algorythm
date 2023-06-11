T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N개의 줄에 M개의 문자
    arr = [str(input()) for _ in range(N)]

    minV = N * M
    for a in range(N-2):
        for b in range(a+1, N-1):
            cnt = 0     # 바꿔야하는 칸 수
            for i in range(a+1):      # 첫번째 칸
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1

            for i in range(a+1, b+1):  # 두번째 칸
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1

            for i in range(b+1, N):  # 세번째 칸
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            minV = min(minV, cnt)
    print(f'#{test_case}', minV)
