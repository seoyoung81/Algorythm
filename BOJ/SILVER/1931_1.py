
N = int(input())    # 회의의 수
info = []
for _ in range(N):
    info.append(tuple(map(int, input().split())))

info = sorted(info, key=lambda a: a[0])
info = sorted(info, key=lambda a: a[1])


lst = [info[0]]
for i in range(1, N):
    if lst[-1][1] <= info[i][0]:
        lst.append(info[i])
print(len(lst))






