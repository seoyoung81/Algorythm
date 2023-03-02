# import sys
# sys.stdin = open('input.txt')

T = 1
for _ in range(1, T + 1):
    test_case = int(input())    # test case number
    ladder = [list(map(int, input().split())) for _ in range(10)]  # ladder 정보 2차원 리스트로 입력 받기

    start = ladder[-1].index(2)     # 마지막 행의 2인 곳에서 출발하자

    # 델타 탐색
    dx = [-1, 0, 0] # 하는 없음 / 상 우 좌
    dy = [0, 1, -1]

    ni = start
    nj = 9
    k = 0   # 시작은 일단 위로

    while ni != 0:  # 0행에 올 때 까지
        ni = ni + dx[k]
        nj = nj + dy[k]
        # 왼쪽으로 가기기
        if ladder[ni][nj-1] == 1:   # 왼쪽에 길이 있다면
            k = 2
        # 오른쪽으로 가기
        elif ladder[ni][nj+1] == 1: # 오른쪽에 길이 있다면
            k = 1
        elif ladder[ni][nj-1] == 0 and ladder[ni][nj+1] == 0 and ladder[ni-1][nj] == 1: # 위에 길만 있다면
            k = 0

        print(nj)