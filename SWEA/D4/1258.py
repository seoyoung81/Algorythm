T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    arr =[list(map(int, input().split())) for _ in range(N)]    # 2d arr

    cnt_lst = []
    for lst in arr:
        i = 0
        cnt = 0
        while i != N:
            if lst[i] != 0:  # 행렬 시작
                while lst[i] != 0:  # 0이 나오기 전까
                    i += 1
                    cnt += 1
                cnt_lst.append(cnt)
            else:
                i += 1
    print(cnt_lst)


