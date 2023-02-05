# 색종이
import sys
sys.stdin = open('input.txt')

N = int(input())    # 색종이 장수
'''
1번 색종이는 1로 표시 '1'-> 안 가린 건 1 인 곳
2번 색종이는 2로 표시 '2~3'-> 2번 색종이가 1번 색종이 위로 가면 3이됨 -> 3번 색종이가 안 가린 건 2, 1번 색종이를 가렸는데 3번 색종이가 안 가렸으면 3
3번 색종이는 4로 표시 '4~7'-> 3번 색종이가 1번 가리면 4, 2번 가리면 5 
4번 색종이는 8로 표시 '8~15'-> 최대: 1번 위 2번 위 3번 위 4번: 15, 최소:8
'''
colorpaper = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y, width, length = map(int, input().split())  # 색종이 정보 리스트로 받기
    # (0,0) 가로, 세로
    for i in range(x, x + width):
        for j in range(y, y + length):
            colorpaper[i][j] += 2 ** (N-1)
# print(colorpaper)     # 2의 제곱수로 2차원 리스트 표현
    cnt = 0
    for lst in colorpaper:
        for i in range(N):
            cnt += lst.count(3)
    print(cnt)
        
