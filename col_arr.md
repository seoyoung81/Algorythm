## 2차원 리스트 입력받기
* row_arr
  `row_arr = [list(map(int, input().split())) for _ in range(int(8))]`

* col_arr 로 변경하기
  ```python
  col_arr = [[0] * 8 for _ in range(8)]
    for i in row_arr:
        for j in range(8):
            col_arr[j] += i[j]
  ```

```python
row_sudoku = [list(map(int, input().split())) for _ in range(9)]     # 스도쿠를 2차원 리스트로 입력 받음
    col_sudoku = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            col_sudoku[i][j] = row_sudoku[j][i]
```