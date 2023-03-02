# import sys
# sys.stdin = open('input.txt')

# 빙고판 2차원 리스트
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자
numbers = []
for _ in range(5):      # 1차원으로 받아서 몇 번째인지 인덱스로 세주기
    number = list(map(int, input().split()))
    for i in range(5):
        numbers.append(int(number[i]))

# 숫자가 해당되면 그 칸을 0으로 만들자
# 가로 세로 대각선 의 합이 0이 되는 순간까지
cnt_lst = [[0] * 5 for _ in range(5)]
# k_lst = []
for k in range(25):
    for i in range(5):
        for j in range(5):
            if numbers[k] == bingo[i][j]:    # 숫자를 부르면
                bingo[i][j] = 0

    # print(bingo)
    # 합 구하기

    for p in range(5):
        # 가로
        if bingo[p][0] + bingo[p][1] + bingo[p][2] + bingo[p][3] + bingo[p][4] == 0:
            cnt_lst[p][0] = 1   # 합이면 2차원 리스트 정해진 구역을 1로 만들기
        # 세로
        if bingo[0][p] + bingo[1][p] + bingo[2][p] + bingo[3][p] + bingo[4][p] == 0:
            cnt_lst[p][1] = 1
        # 대각선 1
        if bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4] == 0:
            cnt_lst[0][2] = 1

        # 대각선 2
        if bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0] == 0:
            cnt_lst[0][3] = 1


    print(cnt_lst)
    total = 0
    for lst in cnt_lst:
        total += lst.count(1)
        if total >= 3:
            print(k+1)
            exit()


# 탈출 못했을 때 푼 방법
'''
k_lst 에 k 다 추가해서 가장 첫번째꺼 꺼내기
'''



