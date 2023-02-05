N = int(input())

for i in range(1, N+1):
    print(('*' * i).rjust(N))   # 오른쪽 정렬 .rjust(N)
    print(('*' * i).ljust(N))   # 왼쪽 정렬 .rjust(N)
    