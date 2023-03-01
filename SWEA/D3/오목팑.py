T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # 오목 판의 크기 N x N
    omok = [list(map(str, input())) for _ in range(N)]  # 오목 정보 입력 받기
    col_omok = list(map(list, zip(*omok)))  # 세로 구하기 쉽게 전치 행렬 구하기
    # print(col_omok)

    # 무조건 5개만 연속이면 된다
    result = 0
    for i in range(N):
        for j in range(N):
            if ''.join(omok[i][j:j+5]) == 'ooooo':   # 가로 5개
                result = 1
            if ''.join(col_omok[i][j:j+5]) == 'ooooo':   # 세로 5개
                result = 1

            diagonal1 = ''
            diagonal2 = ''
            if omok[i][j] == 'o':   # 일단 시작이 o라면 -> 대각선 검사
                for k in range(5):
                    if 0 <= i+k < N and 0 <= j+k < N:
                        diagonal1 += omok[i+k][j+k]
                    if 0 <= i-k < N and 0 <= j+k < N:
                        diagonal2 += omok[i-k][j+k]

                if diagonal1 == 'ooooo':
                    result = 1
                if diagonal2 == 'ooooo':
                    result = 1

    # result 판단
    if result == 1: # 한 줄이라도 완성된게 있다면
        print(f'#{test_case}', 'YES')
    else:
        print(f'#{test_case}', 'NO')



