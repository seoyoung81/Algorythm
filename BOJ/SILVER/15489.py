import math
R, C, W = map(int, input().split()) # R 번째 줄 C 번째 수를 위 꼭짓점으로 하는 한 변이 4개

# # 첫번째 수 구하기
# first = math.comb(R-1, C-1)
# print(first)
#
# # 두번째 줄 구하기
# i = 1
# total = first
# total += math.comb(R-1+i, C-1)
# print(total)
# total += math.comb(R-1+i, C-1+i)
#
# print(total)

total = 0
# 전체 구하기
for i in range(W):  # 줄 개수 만큼 반복 시킴
    for j in range(i+1):
        total += math.comb(R-1+i, C-1+j)
print(total)