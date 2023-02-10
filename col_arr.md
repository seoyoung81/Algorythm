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