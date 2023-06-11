M, N, H = map(int, input().split())     # 가로 세로 높이
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato[k][j][i] == 1:    # 익은 토마토 라면
                for di, dj, dk in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)): # 상하좌우 위 아래
                    ni = i + di
                    nj = j + dj
                    nk = k + dk
                    if 0 <= ni < M and 0 <= nj < N and 0 <= nk < H:
                        if tomato[nk][nj][ni] == 0: # 익지 않은 토마토라면
                            tomato[nk][nj][ni] = 1  # 익히기
print(tomato)