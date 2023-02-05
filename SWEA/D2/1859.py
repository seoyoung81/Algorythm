T = int(input())    # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())    # 자연수
    numbers = list(map(int, input().split())) # 각 날의 매매가 (N개의 자연수)
    
    result = 0
    max_num = 0
    for i in range(len(numbers)-1, -1, -1):   # 거꾸로 가자
        if numbers[i] > max_num:            # numbers[i]가 max_num 보다 크면
            max_num = numbers[i]            # max_num 에 numbers[i]를 할당
        else:
            result += max_num - numbers[i]      # 그게 아니라면, result에 max_num - numbers[i] max_num에 numbers[i]를 판다
    print(f'#{test_case} {result}')

'''
3 5 9 -> 9 * 2 - (3 + 5)
1 1 3 1 2 -> 3 * 2 - (1 + 1) + 2 - 1
'''
