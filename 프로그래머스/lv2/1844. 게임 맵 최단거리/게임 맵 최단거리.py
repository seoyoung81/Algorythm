from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1 
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
        
    return answer