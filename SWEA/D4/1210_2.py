T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 100 x 100 arr
    N = 100
    start_y = ladder[-1].index(2)   # 마지막 줄 2인 곳의 인덱스에서 시작
    start_x = 99

    while True:
        if start_y - 1 >= 0 and ladder[start_x][start_y-1] == 1:  # 왼쪽으로 갈 수 있다면
            ladder[start_x][start_y] = 0  # 0으로 만들어서 다시 올 수 없게 하
            start_y -= 1    # 이동
        elif start_y + 1 < N and ladder[start_x][start_y+1] == 1:   # 오른쪽으로 갈 수 있다면
            ladder[start_x][start_y] = 0
            start_y += 1
        elif start_x - 1 >= 0 and ladder[start_x-1][start_y] == 1:
            # ladder[start_x-1][start_y] = 0
            start_x -= 1
        else:
            print(start_y)
            break


