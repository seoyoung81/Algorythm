def dfs():
    # 종료 조건
    if len(lst) == M:
        print(*lst)
        return

    # 하부 호출
    for i in numbers:
        if len(lst) == 0:
            lst.append(i)
            dfs()
            lst.pop()
        else:
            if lst[-1] < i:
                lst.append(i)
                dfs()
                lst.pop()




N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
lst = []
dfs()