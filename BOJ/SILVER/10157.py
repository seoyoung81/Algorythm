C, R = map(int, input().split())    # 가로 / 세로
number = int(input())   # 자리 번호
N = C * R   # 번호 개수

# 번호가 자리 개수보다 많은 경우
if number > N:
    print(0)

arr = [[0] * (R) for _ in range(C)]

dx = [0, 1, 0, -1]  #  우 하 좌 상
dy = [1, 0, -1, 0]

i = 0
j = 0
cnt = 2
arr[0][0] = 1
k = 0
while cnt != N+1:
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



# 번호 찾기
for i in range(C):
    for j in range(R):
        if arr[i][j] == number:
            print(i+1, j+1)

