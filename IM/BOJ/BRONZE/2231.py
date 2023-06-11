N = int(input())    # N 의 생성자 구하기

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    if sum(nums) + i == N:
        print(i)
        break

    if i == N:
        print(0)