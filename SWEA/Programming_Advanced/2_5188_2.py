def dfs(i, j, sm):
    global result

    # 종료 조건
    if i == N-1 and j == N-1:   # 가장 오른쪽 아래에 도착했으면
        if result > sm:     # 결과보다 총 합이 더 작으면 작은값을 result 에 할당
            result = sm
        return
    
    # 가지 치기 -> sm 이 도착하기도 전에 결과값을 넘어서면
    elif result < sm:
        return

    # 하부 호출
    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if ni < N and nj < N:
            dfs(ni, nj, sm+arr[ni][nj])     # 더해주기


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 987654321
    dfs(0, 0, arr[0][0])
    print(f'#{test_case}', result)