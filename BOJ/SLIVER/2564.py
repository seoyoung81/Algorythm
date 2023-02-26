# import sys
# sys.stdin = open('input.txt')

x, y = map(int, input().split())    # 가로, 세로
# 둘레
round = (2 * (x + y))

N = int(input())    # 상점의 개수
infos = []
for _ in range(N+1):    # 동근 위치, 상점 정보 입력 받기
    infos.append(list(map(int, input().split())))

cordinate = []
# 좌표 다시 정해주기
for lst in infos:
    if lst[0] == 1:     # 북쪽인 경우
        cordinate.append([lst[1], y, 0, 0])
    elif lst[0] == 2:   # 남쪽인 경우
        cordinate.append([lst[1], 0, 0, 0])
    elif lst[0] == 3:   # 서쪽인 경우
        cordinate.append([0, y-lst[1], 0, 0])
    else:               # 동쪽인 경우
        cordinate.append([x, y-lst[1], 0, 0])

# 동근이
a, b = cordinate[-1][0], cordinate[-1][1]

# 길이 구하기
for i in range(N):
    if a == x or b == 0:    # 동근이가 동 남 쪽에 있는 경우
        if cordinate[i][0] == 0 or cordinate[i][1] == y:    # 북 서 쪽에 있는 상점은
            cordinate[i][2] = (cordinate[i][0] + cordinate[i][1] + a + b)
            cordinate[i][3] = round - cordinate[i][2]
        else:   # 동 남 쪽에 있는 경우
            cordinate[i][2] = abs(cordinate[i][0] + cordinate[i][1] - (a + b))
            cordinate[i][3] = round - cordinate[i][2]
    elif a == 0 or b == y:                    # 동근이가 북 서 쪽에 있는 경우
        if cordinate[i][0] == 0 or cordinate[i][1] == y:    # 북 서 쪽에 있는 상점은
            cordinate[i][2] = abs(cordinate[i][0] + cordinate[i][1] - (a + b))
            cordinate[i][3] = round - cordinate[i][2]
        else:   # 동 남 쪽에 있는 경우
            cordinate[i][2] = (cordinate[i][0] + cordinate[i][1] + a + b)
            cordinate[i][3] = round - cordinate[i][2]

# 최단 거리 구하기
distance = []
for i in range(N):
    if cordinate[i][2] <= cordinate[i][3]:
        distance.append(cordinate[i][2])
    else:
        distance.append(cordinate[i][3])

# 합 출력
print(sum(distance))



