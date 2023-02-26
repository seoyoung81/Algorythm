import sys
sys.stdin = open('input.txt')

N = int(input())    # 색종이 개수
color = [[0] * 101 for _ in range(101)]     # 2d arr

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            color[i][j] = 1

# print(color)
count = 0

for lst in color:
    count += lst.count(1)

print(count)
