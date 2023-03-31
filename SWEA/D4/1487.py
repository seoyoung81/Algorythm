def dfs(n, sm):
    global cnt

    # 가지 치기
    if sm > W:
        return

    # 종료 조건
    if n == N:
        if sm == W:     # 합이 W가 되면 종료
            cnt += 1
        return

    # 하부 호출
    # 다음 원소를 포함하면
    dfs(n+1, sm+number[n])
    # 다음 원소를 포함하지 않으면
    dfs(n+1, sm)


T = int(input())
for test_case in range(1, T + 1):
    N, W = map(int, input().split())
    number = list(map(int, input().split()))

    cnt = 0
    dfs(0, 0)
    print(cnt)