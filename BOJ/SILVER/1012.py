T = int(input())    
for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())    # 가로/세로, 배추 개수
    arr = [[0]*(M+1) for _ in range(N+1)]   # 배추 위치 담기
    visited = [[0]*(M+1) for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            if arr[i][j] == 1 and visited[i][j] == 0:  # 배추가 있고 방문한 적이 없다면  # 사방을 확인하자
                visited[i][j] = 1
                for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    visited[ni][nj] = 1
                    if arr[di][dj] == 1:    # 주변에 배추가 있다면
                        cnt += 1
            if cnt >= 1:
                result += 1

            print(cnt)
    print(result)
