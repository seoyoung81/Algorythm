def dfs(cur, total, lst):
    global cnt

    # 종료 조건
    if cur == N:
        # print(lst)
        if len(lst) != 0:
            if total == S:
                cnt += 1
                return


    # 하부 호출
    if cur <= N-1:
        # 포함
        dfs(cur+1, total + numbers[cur], lst + [numbers[cur]])
        # 포함 X
        dfs(cur+1, total, lst)



N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
dfs(0, 0, [])
print(cnt)