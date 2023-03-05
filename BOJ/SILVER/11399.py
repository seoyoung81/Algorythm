N = int(input())    # 사람 수
time = sorted(list(map(int, input().split())))  # 정렬해야 시간 줄어 든다

total = 0
for i in range(N):
    total += time[i] * (N-i)
print(total)