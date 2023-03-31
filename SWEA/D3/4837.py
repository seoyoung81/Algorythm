def dfs(n, sm, i):
    global cnt

    # 종료 조건
    if i == N:
        if sm == K:     # 합이 K가 되면 종료
            cnt += 1
        return

    if n <= 11:
        # 하부 호출
        # 다음 원소를 포함하면
        dfs(n+1, sm+number[n], i+1)
        # 다음 원소를 포함하지 않으면
        dfs(n+1, sm, i)



T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    number = [i for i in range(1, 13)]

    cnt = 0
    dfs(0, 0, 0)
    print(f'#{test_case}', cnt)