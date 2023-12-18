number = list(map(int, input().split()))

max_num = max(number)
min_num = min(number)
start = min(max_num, min_num)
for i in range(start, 1000000):
    cnt = 0
    for num in number:
        if i%num == 0:
            cnt += 1
        if cnt == 3:
            print(i)
            break
    if cnt == 3:
        break
