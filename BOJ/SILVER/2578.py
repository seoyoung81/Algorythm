import sys
sys.stdin = open('input.txt')

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
a = b = c1 = c2 = 0
while a != 0 and b != 0 and c1 != 0 and c2 != 0:
    for i in range(25):
        for p in range(5):
            for q in range(5):
                if numbers[i] == bingo[p][q]:   # 숫자 부른게 같다면
                    bingo[p][q] = 0
                    break

    for i in range(5):
        a = sum(bingo[i])
        c1 = sum(bingo[i][i])
        for j in range(5):
            b = sum(bingo[j][i])

                    # b, c1, c2 안 구함




print(bingo)




