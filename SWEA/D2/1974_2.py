T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    col_sudoku = list(map(list, zip(*sudoku)))

    result = 1
    # 가로 세로
    for lst in sudoku:
        for i in range(9):
            if lst.count(i+1) != 1:
                result = 0
    for lst in col_sudoku:
        for i in range(9):
            if lst.count(i+1) != 1:
                result = 0

    # 네모
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                total_lst = []
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        total_lst.append(sudoku[p][q])
                # print(total_lst)
                if sorted(total_lst) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    result = 0

    print(f'#{test_case}', result)
