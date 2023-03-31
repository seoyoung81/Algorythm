def dfs(sm, n):
    global cnt

    # 종료 조건
    if n == N:
        if sm == K:     # 합이 K이면
            cnt += 1
        return


    # 하부 호출
    # 다음 수를 포함하면
    dfs(sm+A[n], n+1)
    # 다음 수를 포함하지 않으면
    dfs(sm, n+1)




T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N 개의 수, 그 합이 K
    A = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{test_case}', cnt)

