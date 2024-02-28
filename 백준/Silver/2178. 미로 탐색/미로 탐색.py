from collections import deque
n, m = map(int, input().split())
miro = []

for _ in range(n):
  lst = list(map(int, input()))
  miro.append(lst)

queue = deque([((0, 0))])

dx = [0 ,0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    i, j = queue.popleft()
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx <n and 0 <= ny <m:
          if miro[nx][ny] == 1:
            queue.append((nx, ny))
            miro[nx][ny] = miro[i][j] + 1

print(miro[n-1][m-1])