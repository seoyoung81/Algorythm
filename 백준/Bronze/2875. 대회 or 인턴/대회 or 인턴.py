N, M, K = map(int, input().split())
# 여, 남, 반드시 인턴십에 참여해야 하는 학생

team = 0
while True :
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)<K:
        break
    team+=1
print(team)