T = 10
for test_case in range(1, T + 1):
    n = int(input())    # 찾아야 하는 회문의 길이
    arr = [list(map(str, input())) for _ in range(8)]   # 8X8 2d arr
    # print(arr)
    col_arr = list(map(list, zip(*arr)))    # trans arr
    # print(col_arr)

    cnt = 0     # 회문 개수
    for j in range(8):
        for i in range(8-n+1):
            word = arr[j][i:i+n]
            if word == word[::-1]:  # 뒤집어도 똑같으면 회문!
                cnt += 1

    for j in range(8):
        for i in range(8-n+1):
            word = col_arr[j][i:i+n]
            if word == word[::-1]:  # 뒤집어도 똑같으면 회문!
                cnt += 1

    print(f'#{test_case}', cnt)