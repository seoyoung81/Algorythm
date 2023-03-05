N = int(input())    # N 보다 작거나 같은 한수의 개수 < 1000

cnt = 0

# 두자리 수 까지
if N < 100:
    cnt += N

# 세자리 수
else:
    cnt += 99
    numbers = [str(i) for i in range(100, N+1)]
    for num in numbers:
        if int(num[1]) - int(num[0]) == int(num[2]) - int(num[1]):
            cnt += 1

print(cnt)