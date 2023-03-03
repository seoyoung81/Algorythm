T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    arr =[list(map(int, input().split())) for _ in range(N)]    # 2d arr
    col_arr = list(map(list, zip(*arr)))    # trans arr


    print(arr)
    print(col_arr)

    col_cnt = [[] * N]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                col_cnt +=
