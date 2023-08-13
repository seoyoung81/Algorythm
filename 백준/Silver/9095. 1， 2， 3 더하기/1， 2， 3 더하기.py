T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    num = [0] * 12
    num[1] = 1
    num[2] = 2
    num[3] = 4
    for i in range(4, n+1):
        num[i] = num[i-3] + num[i-2] + num[i-1]
    print(num[n])