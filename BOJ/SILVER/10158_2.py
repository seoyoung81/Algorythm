w, h = map(int, input().split())    # 가로 세로
p, q = map(int, input().split())    # 초기 위치
t = int(input())    # 움직일 횟 수

dx = 1
dy = 1
dy = 1
cnt = 0
while cnt != t:
    p = p + dx
    q = q + dy
    cnt += 1
    if p == w and q == h:
        dx = -1
        dy = -1
    elif p == 0 and q == 0:
        dx = 1
        dy = 1
    elif p == w:
        dx = -1
    elif p == 0:
        dx = 1
    elif q == h:
        dy = -1
    elif q == 0:
        dy = 1
print(p, q)