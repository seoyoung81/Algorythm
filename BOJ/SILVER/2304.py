# import sys
# sys.stdin = open('input.txt')

N = int(input())    # 기둥의 개수
chango_lst = []
idx_lst = []
for _ in range(N):
    idx, height = map(int, input().split())     # x, y
    chango_lst.append([idx, height])

# x 좌표 크기로 정
chango_lst = sorted(chango_lst)

# 가장 큰 값 구하기, idx 구하기
middle = chango_lst[0][1]
m_idx = 0
for i in range(1, N):
    if middle < chango_lst[i][1]:
        middle = chango_lst[i][1]

    if chango_lst[i][1] == middle:
        m_idx = i

# print(chango_lst)

# 0 부터 middle 까지 감소하면 삭제
for idx in range(1, m_idx):
    if chango_lst[idx-1][1] > chango_lst[idx][1]:   # 감소하면
        chango_lst[idx] = chango_lst[idx-1]

# middle 부터 끝까지 증가하면 삭제
for idx in range(N-1, m_idx+1, -1):
    if chango_lst[idx-1][1] < chango_lst[idx][1]:   # 증가하면
        chango_lst[idx-1] = chango_lst[idx]

# print(chango_lst)

total = 0
for i in range(m_idx):
    total += chango_lst[i][1] * (chango_lst[i+1][0] - chango_lst[i][0])

# print(total)    # 32

for i in range(N-2, m_idx-1, -1):
    total += chango_lst[i+1][1] * (chango_lst[i+1][0] - chango_lst[i][0])

# print(total)    # 88

total += middle
print(total)

