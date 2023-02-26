# import sys
# sys.stdin = open('input.txt')

N = int(input())    # 1m^2 당 참외의 개수
melon = [list(map(int, input().split())) for _ in range(6)]   # 입력받기

# 전체 넓이 구하기
x_lst = []
y_lst = []
for lst in melon:
    if lst[0] == 1 or lst[0] == 2:
        x_lst.append(lst[1])
    else:
        y_lst.append(lst[1])

x = max(x_lst)
y = max(y_lst)
entire_area = x * y

# 작은 사각형 넓이 구하기
a = b = 0
for lst in melon:
    if lst[0] == 1 or lst[0] == 2:
        if lst[1] == x:     # 최댓값이라면
            a = melon.index(lst)
    else:
        if lst[1] == y:
            b = melon.index(lst)

# 가로
if a == 5:
    wide = abs(melon[0][1] - melon[4][1])
else:
    wide = abs(melon[a-1][1] - melon[a+1][1])
# 세로
if b == 5:
    length = abs(melon[0][1] - melon[4][1])
else:
    length = abs(melon[b-1][1] - melon[b+1][1])

area = wide * length

# 진짜 넓이에 해당하는 참외
result = (entire_area - area) * N
print(result)


