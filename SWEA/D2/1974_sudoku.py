# import sys
# sys.stdin = open('input.txt')
T = int(input())    # 테스트 케이스의 개수

for tc in range(1, T+1):
    row_sudoku = [list(map(int, input().split())) for _ in range(9)]     # 스도쿠를 2차원 리스트로 입력 받음
    col_sudoku = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            col_sudoku[i][j] = row_sudoku[j][i]

    print(row_sudoku)
    print(col_sudoku)

