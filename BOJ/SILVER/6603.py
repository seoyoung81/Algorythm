def dfs():
    if len(lst) == 6:
        print(*lst)
        return

    for i in lotto:
        if len(lst) == 0:
            lst.append(i)
            dfs()
            lst.pop()
        else:
            if i not in lst and lst[-1] < i:
                lst.append(i)
                dfs()
                lst.pop()


while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break

    k = s[0]
    lotto = sorted(s[1:])
    lst = []
    dfs()
    print()