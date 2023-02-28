N = int(input())


for i in range(1, N):   # 두번째 수는 1부터 N-1 까지 중 하나라고 생각
    memo = [0] * (N + 1)  # 모든 수를 저장할 memo 리스트
    memo[0] = N  # 첫번째 수는 주어진 입력 값
    memo[1] = i     # 두번째 수는 계속 반복
    memo[i+1] = memo[i-1] - memo[i]

    print(memo)
