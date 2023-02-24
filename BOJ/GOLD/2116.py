'''
입력 순서 A, B, C, D, E, F
짝 A F / B D / C E
'''

N = int(input())    # 주사위의 개수
# N 개의 주사위 정보를 받자
numbers = [list(map(int, input().split())) for _ in range(N)]   # A, B, C, D, E, F  2d arr

# down = numbers[0][0]    # 바닥이 A
# up = numbers[0][5-0]    # 바닥이 F
#
# for i in range(5):
#     if numbers[1][i] == up:     # 첫번째 천장이랑 같은 숫자가
#         down2 = numbers[1][i]   # 바닥
#         up2 = numbers[1][6-i]   # 천장


for i in range(3):          # 바닥에 처음 올 수 있는 면 3개
    cnt = 0
    j = 0
    while cnt != N:
        down = numbers[j][i]
        up = numbers[j][5-i]
        for k in range(5):
            if numbers[j+1][k] == up:   # 다음 주사위에서 up이 될 수 있는 면을 정하면
                down = numbers[j+1][k]
                up = numbers[j+1][5-k]
                j += 1
                cnt += 1

        print(down, up)
#
#

total = 0
reverse = [5, 3, 4, 1, 2, 0]        # 0번 인덱스에 짝 5, 1번 인덱스에 짝 3, 2번 리스트에 짝 4
for floor in range(1, 7):
    sum = 0
    for th in numbers:
        top = th[reverse[th.index(floor)]]
        if floor + top == 11:   # 위 아래가 5, 6인 경우
            sum += 4
        elif floor == 6 or top == 6:
            sum += 5
        else:
            sum += 6
        floor = top
    if sum > total:
        total = sum
    print(total)


min_number = min(numbers)
for i in range(5):
    if numbers[0][i] == min_number:
        if numbers[0][5-i] != 6:
            total += 6
        elif numbers[0][5-i] == 6:
            total += 5


