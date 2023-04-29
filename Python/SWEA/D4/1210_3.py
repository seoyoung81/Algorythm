T = 10
for test_case in range(1, T + 1):
    num = int(input())  # test case number
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 100 x 100 arr

    x = 99
    y = ladder[-1].index(2) # 2인 곳에서 시작하자

    while True:
        if y-1 >= 0 and ladder[x][y-1] == 1:
            ladder[x][y] = 0
            y -= 1
        elif y+1 < 100 and ladder[x][y+1] == 1:
            ladder[x][y] = 0
            y += 1
        elif x-1 >= 0 and ladder[x-1][y] == 1:
            ladder[x][y] = 0
            x -= 1
        else:
            print(y)
            break
