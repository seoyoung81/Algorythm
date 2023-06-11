def dfs(cur, sm, lst):
    global result

    # 종료 조건
    if cur == N:
        if sm >= B:
            # print(lst)
            result = min(result, sm)
            return

    # 하부 호출
    if cur < N:
        dfs(cur+1, sm + height[cur], lst + [height[cur]])
        dfs(cur+1, sm, lst)


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = sum(height)
    dfs(0, 0, [])
    print(f'#{test_case}', result-B)

#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
