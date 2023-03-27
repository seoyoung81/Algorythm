def perm(i, k):
    if i == k:
        arr.append(p)
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
    arr = []
    p = [0] * 6
    used = [0] * 6
    perm(0, 6)
    print(arr)

# if p[0] == p[1] == p[2]:
#     run += 1
# elif p[3] == p[4] == p[5]:
#     run += 1
# elif p[0] + 1 == p[1] and p[1] + 1 == p[2]:
#     triplet += 1
# elif p[3] + 1 == p[4] and p[4] + 1 == p[5]:
#     triplet += 1
# print(triplet + run)
# return triplet + run




