T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # 오목 판의 크기 N x N
    omok = [list(map(str, input())) for _ in range(N)]  # 오목 정보 입력 받기
    col_omok = list(map(list, zip(*omok)))  # 세로 구하기 쉽게 전치 행렬 구하기
    # print(col_omok)

    # 무조건 5개만 연속이면 된다
    result = 0
    diagonal1 = []
    diagonal2 = []
    for i in range(N):
        diagonal1.append(omok[i][i])    # 대각선 값들을 모두 리스트에 추가(i=j)
        diagonal2.append(omok[i][N-1-i])    # 대각선 값 리스트에 추가 (i!=j)

        for j in range(N):
            if ''.join(omok[i][j:j+5]) == 'ooooo':   # 가로 5개
                result = 1
            if ''.join(col_omok[i][j:j+5]) == 'ooooo':   # 세로 5개
                result = 1

    if 'ooooo' in ''.join(diagonal1):   # 오목이 완성된게 있으면
        result = 1

    if 'ooooo' in ''.join(diagonal2):
        result = 1

    # result 판단
    if result == 1:
        print(f'#{test_case}', 'YES')
    else:
        print(f'#{test_case}', 'NO')



