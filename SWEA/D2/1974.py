T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    col_sudoku = list(map(list, zip(*sudoku)))

    # 결과
    result = 1
    # 가로 줄 확인
    for lst in sudoku:
        for i in range(1, 10):
            if lst.count(i) != 1:   # 숫자가의 개수가 1개가 아니라면
                result = 0

    # 세로 줄 확인
    for lst in col_sudoku:
        for i in range(1, 10):
            if lst.count(i) != 1:   # 숫자가의 개수가 1개가 아니라면
                result = 0

    # 네모 칸 확인
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                sudoku_lst = []
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        sudoku_lst.append(sudoku[p][q])

                if sorted(sudoku_lst) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    result = 0

    print(f'#{test_case}', result)