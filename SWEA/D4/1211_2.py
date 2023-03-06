T = 10
for test_case in range(1, T + 1):
    tc = int(input())   # test case number
    ladder = [list(map(int, input().split())) for _ in range(100)]

    cnt_lst = [0] * 101
    for i in range(100):
        if ladder[0][i] == 1:   # 시작할 수 있는 곳에서만 출발하기
            j = 0
            visited = [[0] * 100 for _ in range(100)]   # 방문한 곳은 1찍어서 다시 오지 않기
            cnt = 0
            while True:
                if i+1 < 100 and ladder[j][i+1] == 1 and visited[j][i+1] == 0:  # 오른쪽으로 가기
                    visited[j][i] = 1
                    i += 1
                    cnt += 1
                elif i-1 >= 0 and ladder[j][i-1] == 1 and visited[j][i-1] == 0: # 왼쪽으로 가기
                    visited[j][i] = 1
                    i -= 1
                    cnt += 1
                elif j+1 < 100 and ladder[j+1][i] == 1 and visited[j+1][i] == 0:    # 아래로 가기
                    visited[j][i] = 1
                    j += 1
                    cnt += 1
                else:
                    cnt_lst[i] = cnt
                    break

    # 최솟값의 인덱스 구하기
    a = min(cnt_lst)
    print(cnt_lst)

    for i in range(100, -1, -1):
        if cnt_lst[i] == a:
            print(i)
            break


