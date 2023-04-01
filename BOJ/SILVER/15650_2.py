def dfs():
    # 종료 조건
    if len(lst) == M:
        print(*lst)
        return

    # 하부 호출
    for i in range(1, N+1):
        if len(lst) == 0:   # 원소가 한개도 없으면
            lst.append(i)
            dfs()
            lst.pop()
        else:
            if i not in lst and i > lst[-1]:    # i가 lst 에 없고 마지막 원소보다 큰 경우에
                lst.append(i)
                dfs()
                lst.pop()


N, M = map(int, input().split())
lst = []
dfs()
