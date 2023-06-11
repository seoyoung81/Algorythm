T = 10
for test_case in range(1, T + 1):
    num = int(input())  # test case number
    arr = [list(map(str, input())) for _ in range(100)]     # 100X100 2d arr
    col_arr = list(map(list, zip(*arr)))    # trans arr

    cnt = 0
    for n in range(100, 0, -1): # 회문의 길이
        for i in range(100):
            for j in range(100-n+1):
                word1 = arr[i][j:j+n]
                word2 = col_arr[i][j:j+n]
                if word1 == word1[::-1]:      # 앞 뒤가 같으면
                    cnt += 1
                if word2 == word2[::-1]:
                    cnt += 1

        if cnt >= 1:    # 회문을 하나라도 찾는 순간
            print(f'#{num}', n)
            break
