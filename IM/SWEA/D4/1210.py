# import sys
# sys.stdin = open('input.txt')

T = 10
for _ in range(1, T + 1):
    test_case = int(input())    # test case number
    ladder = [list(map(int, input().split())) for _ in range(100)]  # ladder 정보 2차원 리스트로 입력 받기

    start = ladder[-1].index(2)     # 마지막 행의 2인 곳에서 출발하자

    # # 델타 탐색
    # dx = [-1, 0, 0] # 하는 없음 / 상 우 좌
    # dy = [0, 1, -1]

    ni = start
    nj = 99     # 행
    # k = 0   # 시작은 일단 위로

    while True:  # 0행에 올 때 까지
        if ni + 1 < 100 and ladder[nj][ni+1] == 1:    # 오른쪽이 1이라면
            ladder[nj][ni] = 0  # 다시 안 올거니까 0으로 만들고
            ni = ni + 1   # 오른쪽으로 가기
        elif 0 <= ni - 1 and ladder[nj][ni-1] == 1:  # 왼쪽이 1이라면
            ladder[nj][ni] = 0  # 다시 안 올거니까 0으로 만들고
            ni = ni - 1 # 왼쪽으로 가기
        elif nj - 1 >= 0 and ladder[nj-1][ni] == 1:     # 위쪽에 길이 있으면
            nj = nj - 1
        else:
            print(f'#{test_case}', ni)
            break


