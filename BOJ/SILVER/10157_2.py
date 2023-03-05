C, R = map(int, input().split())    # 가로 세로
number = int(input())   # 자리 번호
arr = [[0] * R for _ in range(C)]

if number > C * R:
    print(0)

cnt = 2
arr[0][0] = 1
i = j = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
k = 0

while cnt != C * R + 1:
    ni = i + dx[k]
    nj = j + dy[k]

    if 0 <= ni < C and 0 <= nj < R and arr[ni][nj] == 0:
        arr[ni][nj] = cnt
        cnt += 1
        i = ni
        j = nj
    else:
        k += 1
        if k > 3:
            k = 0

# print(arr)
for i in range(C):
    for j in range(R):
        if arr[i][j] == number:
            print(i+1, j+1)