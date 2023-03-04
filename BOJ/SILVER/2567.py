N = int(input())    # 색종이 개수
board = [[0] * 102 for _ in range(102)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1     # 색종이 자리에 1 할당

# 둘레 측정
# 0에서 1이 되는 순간, 1에서 0이 되는 순간 개수
cnt = 0
# 세로 먼저 계산
for lst in board:
    for i in range(101):
        if lst[i] == 0 and lst[i+1] == 1: # 0이었다가 1이 되는 곳
            cnt += 1
        elif lst[i] == 1 and lst[i+1] == 0: # 1이었다가 0이 되는 곳
            cnt += 1

# 가로 계산
col_board = list(map(list, zip(*board)))
for lst in col_board:
    for i in range(101):
        if lst[i] == 0 and lst[i+1] == 1: # 0이었다가 1이 되는 곳
            cnt += 1
        elif lst[i] == 1 and lst[i+1] == 0: # 1이었다가 0이 되는 곳
            cnt += 1
print(cnt)