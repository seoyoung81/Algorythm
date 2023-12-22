N = int(input())

for num in range(2, N+1):
    if N < num:
        break
    while N%num==0:
        N = N/num
        print(num)
