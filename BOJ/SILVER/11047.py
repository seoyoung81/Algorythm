N, K = map(int, input().split())
coin = []
cnt = 0
for _ in range(N):
    coin.append(int(input()))

K_lst = [K]

for i in range(N-1, -1, -1):
    q = K_lst[-1] // coin[i]    # 몫
    r = K_lst[-1] % coin[i]     # 나머지

    # print(q, r)
    if q != 0:    # 1 개라도 들어가면
        cnt += q
        K_lst.append(r)

print(cnt)