N = int(input())    # 색종이 장수
board = [[0] * 1001 for _ in range(1001)]
# 좌표 확인 리스트

for _ in range(N):
    x, y, w, h = map(int, input().split())  # 왼쪽 아래 좌표, 너비/높이
    for i in range(x, x+w):
        for j in range(y, y+h):
            board[i][j] = _ + 1    # 가로 세로 바꼈다고 생각하고 좌표 배정


# print(board)

# 색종이 면적 구하기
for i in range(N):
    cnt = 0
    for lst in board:
        cnt += lst.count(i+1)
    print(cnt)

