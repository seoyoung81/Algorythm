N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # a 부터 b 까지 역순으로 만들기
    reverse_arr = arr[a-1:b]
    reverse_arr.reverse()
    arr[a-1:b] = reverse_arr

for i in range(N):
    print(arr[i], end=' ')

