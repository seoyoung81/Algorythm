N = int(input())    # 사람 수
deongchi_lst = []
for _ in range(N):
    x, y = map(int, input().split())    # 몸무게, 키
    deongchi_lst.append([x, y])

# 등수
cnt_lst = []

# 덩치 비교
for i in range(N):
    cnt = 1
    for j in range(N):
        if deongchi_lst[i][0] < deongchi_lst[j][0] and deongchi_lst[i][1] < deongchi_lst[j][1]:
            cnt += 1
    cnt_lst.append(cnt)

print(*cnt_lst)
