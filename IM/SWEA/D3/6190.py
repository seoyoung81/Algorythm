T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N 개의 정수
    numbers = list(map(int, input().split()))
    result = -1

    # 곱한 값 구하기
    for i in range(N):
        for j in range(i+1, N):
            num = str(numbers[i] * numbers[j])
            for k in range(len(num)-1):
                if num[k] > num[k+1]:
                    break
            else:
                result = max(int(num), result)


    print(f'#{test_case}', result)