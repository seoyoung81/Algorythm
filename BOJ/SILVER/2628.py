X, Y = map(int, input().split())    # 가로 세로 <= 100
N = int(input())    # 칼로 잘라야 하는 점선의 개수

width_lst = []
height_lst = []

for _ in range(N):  # 점선의 개수만큼 반복해서 정보 입력 받기
    number, line = map(int, input().split())    # 점선 방향(0 가로 1 세로) / 점선 번호
    if number == 0:
        width_lst.append(line)  # 가로만 담기
    else:
        height_lst.append(line) # 세로만 담기

width_lst.sort()
height_lst.sort()   # 정렬하기

# 가로만 생각
m = len(width_lst)
width_lst2 = [0] * Y
for i in range(m):
    width_lst2.insert(width_lst[i]+i, 1)
print(width_lst2)

# 연속하는 0의 개수가 가장 많은 것 찾기
w_cnt = []
cnt = 0
for i in range(Y+m):
    if width_lst2[i] == 0:
        cnt += 1
    else:
        cnt = 0
    w_cnt.append(cnt)
max_w = max(w_cnt)      # 연속하는 0의 개수가 가장 큰 것


# 세로만 생각
n = len(height_lst)
height_lst2 = [0] * X
for i in range(n):
    height_lst2.insert(height_lst[i]+i, 1)
# print(height_lst2)

h_cnt = []
cnt = 0
for i in range(X+n):
    if height_lst2[i] == 0:
        cnt += 1
    else:
        cnt = 0
    h_cnt.append(cnt)
max_h = max(h_cnt)      # 연속하는 0의 개수가 가장 큰 것

print(max_w * max_h)
