w, h = map(int, input().split())    # 가로 세로
p, q = map(int, input().split())    # 개미의 처음 위치
t = int(input())    # 개미가 움직일 시간

m = 0
dx = dy = 0
while m != t+1:   # 주어진 시간동안 반복
    p = p + dx
    q = q + dy
    m += 1
    if p == w and q == h:
        dx = -1
        dy = -1
    elif p == 0 and q == 0:
        dx = 1
        dy = 1
    elif p == 0:   # 왼쪽 벽에 부딪히면
        dx = 1
    elif p == w:   # 오른쪽 벽에 부딪히면
        dx = -1
    elif q == 0:   # 아래쪽 벽에 부딪히면
        dy = 1
    elif q == h:   # 위쪽 벽에 부딪히면
        dy = -1


print(p, q)