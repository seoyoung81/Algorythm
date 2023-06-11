import sys
sys.stdin = open('input.txt')
T = 10
for test_case in range(1, T + 1):
    tc = int(input())   # test case number
    ladder = [list(map(int, input().split())) for _ in range(100)]     # ladder 2d arr

    cnt_lst = [1000] * 100
    for i in range(100):    # 전체 탐색
        if ladder[0][i] == 1:   # 1인 곳에서 시작하기
            cnt = 0
            visited = [[0] * 100 for _ in range(100)]
            x = 0
            y = i
            while True:
                if y - 1 >= 0 and ladder[x][y-1] == 1 and visited[x][y-1] == 0:     # 왼쪽으로 가기
                    visited[x][y - 1] = 1
                    y -= 1
                    cnt += 1
                elif y + 1 < 100 and ladder[x][y+1] == 1 and visited[x][y+1] == 0:  # 오른쪽으로 가기
                    visited[x][y + 1] = 1
                    y += 1
                    cnt += 1
                elif x + 1 < 100 and ladder[x+1][y] == 1 and visited[x+1][y] == 0:   # 아래로 가기
                    visited[x + 1][y] = 1
                    x += 1
                    cnt += 1
                else:
                    cnt_lst[i] = cnt
                    break


    # print(cnt_lst)
    min_cnt = min(cnt_lst)
    print(f'#{test_case}', cnt_lst.index(min_cnt))


