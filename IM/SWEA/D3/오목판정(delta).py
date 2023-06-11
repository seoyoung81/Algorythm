T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    omok = [list(map(str, input())) for _ in range(N)]  # 2d arr

    # 중복을 방지 하기 위해 검사는 상 우 우하대각선 좌하 대각선
    result = 'NO'
    for start_i in range(N):
        for start_j in range(N):
            if omok[start_i][start_j] == 'o':
                for direct_i, direct_j in ((-1, 0), (0, 1), (1, 1), (-1, 1)):
                    for mul in range(1, 5):
                        next_i = start_i + direct_i * mul
                        next_j = start_j + direct_j * mul
                        if 0 <= next_i < N and 0 <= next_j < N:     # 범위 제한
                            if omok[next_i][next_j] != 'o':     # 실패하는 경우를 생각
                                break
                        else:
                            break

                    else:
                        result = 'YES'




    print(f'#{test_case}', result)


# 우상 우 우하 하