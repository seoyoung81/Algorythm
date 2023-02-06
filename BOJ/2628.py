import sys
sys.stdin = open('input.txt')

width, length = map(int, input().split())   # 가로, 세로
N = int(input()) # 칼로 잘라야 하는 점선의 개수
rectangle = [[0] * width for _ in range(length))    # 가로, 세로에 맞춘 이차원 리스트

for _ in range(N):
    number, line = map(int, input().split())  # 0: 가로, 1: 세로 // 자르고 싶은 번호

    '''
    00001000000
    00001000000
    11111111111
    00001000000
    11111111111
    00001000000
    00001000000
    00001000000
    00001000000
    00001000000
    '''