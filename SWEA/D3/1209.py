T = 10
for test_case in range(1, T + 1):
    tc = int(input())   # test case number
    arr = [list(map(int, input().split())) for _ in range(100)]
    col_arr = list(map(list, zip(*arr)))

    sum_lst = []
    diagonal1 = 0
    diagonal2 = 0
    for i in range(100):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][99-i]
        for j in range(100):
            sum_lst.append(sum(arr[i]))     # 가로 합
            sum_lst.append(sum(col_arr[i]))     # 세로 합

    sum_lst.append(diagonal1)
    sum_lst.append(diagonal2)

    print(f'#{tc}', max(sum_lst))

