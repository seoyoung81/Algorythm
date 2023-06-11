def perm(i, k):
    global ans
    if i == k:
        if p[0] == p[1] == p[2] and (p[3]+2==p[4]+1==p[5]):
            ans = True
        elif p[3] == p[4] == p[5] and (p[0]+2==p[1]+1==p[2]):
            ans = True
        elif p[0] == p[1] == p[2] and p[3] == p[4] == p[5]:
            ans = True
        elif p[0] + 5 == p[1] + 4 == p[2] + 3 == p[3] + 2 == p[4] + 1 == p[5]:
            ans = True
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = num[j]
                used[j] = 1
                perm(i+1, k)
                used[j] = 0


T = int(input())
for _ in range(T):
    num = list(map(int, input()))
    ans = False
    p = [0] * 6
    used = [0] * 6
    perm(0, 6)
    print(ans)






