T = int(input())
for test_case in range(1, T + 1):
    N = float(input())

    '''
    binary = ''
    # 1단계
    a = int(N*2)
    b = N*2 - a
    binary += str(a)
    # 2단계
    c = int(b*2)
    d = b*2 - c
    binary += str(c)
    # 3단계
    e = int(d*2)
    f = d*2 - e
    binary += str(e)
    print(binary)
    '''

    number = [N]
    binary = ''
    for i in range(12):
        a = int(number[-1] * 2)
        b = number[-1] * 2 - a
        number.append(b)
        binary += str(a)
    print(number)
    # print(binary)

    if number[-1] != 0:     # 마지막 정수 값이 0이 아니라면 13자리 이상이 필요한 경우이다
        print(f'#{test_case}', 'overflow')
    else:
        for i in range(13):     # 리스트 개수는 13개 이다.
            if number[i] == 0:
                print(f'#{test_case}', binary[:i])
                break