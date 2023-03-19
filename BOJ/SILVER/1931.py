N = int(input())    # 회의의 수
info = []
for _ in range(N):
    info.append(tuple(map(int, input().split())))

info.sort()
# print(info)

# # 첫번째 원소 다음에 올 수 있는 거 찾기 -> 거기까지만 탐색하면 됨
# for i in range(1, N):
#     if info[0][1] <= info[i][0]:
#         M = i
#         break
# # print(M)

# 완전 탐색
# _________시간초과_________
rslt = 0
for i in range(M):
    lst = []
    lst.append(info[i])     # 0번째 원소부터 시작
    for j in range(i+1, N):
        if j == N-1:
            if lst[-1][1] <= info[N-1][0]:
                lst.append(info[N-1])
        else:
            if lst[-1][1] <= info[j][0]:    # 크거나 같으면
                if info[j][0] == info[j+1][0]:  # 뒤에꺼랑 시작 시간이 같으면
                    if info[j][1] <= info[j+1][1]:  # 끝나는 시간이 더 짧은 쪽 선택
                        lst.append(info[j])
                    else:
                        lst.append(info[j+1])
                else:
                    lst.append(info[j])
            else:   # 뒤에꺼가 더 작음
                pass
    cnt = len(lst)
    rslt = max(cnt, rslt)

print(rslt)






