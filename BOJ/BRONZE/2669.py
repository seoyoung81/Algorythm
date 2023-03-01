rectangle = [[0] * 101 for _ in range(101)]

# 4줄 입력받기
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 직사각형이 있는 곳에 1 찍기
    for i in range(x1, x2):
        for j in range(y1, y2):
            rectangle[i][j] = 1


# 1 개수 세기
cnt = 0
for lst in rectangle:
    cnt += lst.count(1)


print(cnt)
