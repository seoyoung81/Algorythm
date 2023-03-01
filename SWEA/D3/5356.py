import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]

    # 가장 긴 열의 길이 구하기
    max_arr = len(arr[0])
    for i in range(1, 5):
        if max_arr < len(arr[i]):
            max_arr = len(arr[i])

    # 빈 공간 10으로 채우기
    for lst in arr:
        if len(lst) < max_arr:
            while len(lst) != max_arr:
                lst.append(10)

    # 세로로 읽기
    print(f'#{test_case}', end=' ')
    for j in range(max_arr):
        for i in range(5):
            if arr[i][j] == 10:     # 만약에 10이라면 공백이었던 자리니까 넘기기
                pass
            else:
                print(arr[i][j], end='')
    print()