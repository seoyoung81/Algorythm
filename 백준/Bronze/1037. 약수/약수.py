N = int(input()) # 개
number = sorted(list(map(int, input().split()))) # 약수

if len(number) % 2:
    print(number[N//2]**2)
else:
    print(number[0]*number[-1])

