def color(arr, N):
    for n in paper:
        if n <= N:  # 주어진 종이가 더 큰 경우에만
            for i in range(0, N, n):
                for j in range(0, N, n):
                    color.append(arr[i][j])
            print(color)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper = [128, 64, 32, 16, 8, 4, 2, 1]
color = [[], [], [], [], [], [], [], []]

for k in range(8):
    n = paper[k]
    if n <= N:  # 주어진 종이가 더 큰 경우에만
        print(n)
        for i in range(0, N, N-n+1):
            for j in range(0, N, N-n+1):
                color[k].append(arr[i][j])
                print(k)
                print(color)
print(color)
