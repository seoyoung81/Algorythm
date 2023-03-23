arr = [list(map(int, input().split())) for _ in range(10)]

# 전체 탐색
for i in range(10):
    for j in range(10):
        if arr[i][j] == 1: # 색종이를 붙여야 하는 경우에
            # 가로 검사
            if i <= 5:
                if arr[i+1][j] == 1:
                    if arr[i + 1][j] == 1:
