from collections import deque

M, N, H = map(int, input().split())     # 가로 세로 높이
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

cnt = 1
a = 0
cnt_lst = [10]
while cnt != 0:
    a += 1
    check = cnt
    if cnt > 0:
        for k in range(H):
            for j in range(N):
                for i in range(M):
                    if tomato[k][j][i] == 0:
                        cnt += 1
                    elif tomato[k][j][i] == 1:    # 익은 토마토 라면
                        for di, dj, dk in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)): # 상하좌우 위 아래
                            ni = i + di
                            nj = j + dj
                            nk = k + dk
                            if 0 <= ni < M and 0 <= nj < N and 0 <= nk < H:
                                if tomato[nk][nj][ni] == 0: # 익지 않은 토마토라면
                                    tomato[nk][nj][ni] = 1  # 익히기

    if check == cnt:
        cnt = 0
        break

    cnt_lst.append(cnt)
    for i in range(len(cnt_lst)-1):
        if cnt_lst[i] == cnt_lst[i+1]:
            a = 0
            break

# print(tomato)
print(a-1)
