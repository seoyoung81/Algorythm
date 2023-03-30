T = int(input())
for test_case in range(1, T + 1):
    N, number = map(str, input().split())
    N = int(N)  # 문자열의 개수 정수 변환
    a = int(number, 16)     # 문자열 16진수를 10진수로 변환

    lst = list(map(str, bin(a)))    # 10진수를 2진수로 변환 후 리스트로 만들어준다 0b 로 시작하기 때문에
    lst.pop(0)  # 2번 pop(0)를 해준다
    lst.pop(0)

    # str 을 슬라이싱 해도 됨!!
    # a = number[2:]

    lst_1 = (''.join(lst)).zfill(4*N)   # 16진수를 2진수로 바꾸면 4자리로 표시되기 때문에 총 자리수는 4*N 자리이다 -> 남은 자리를 모두 0으로 채우자
    print(f'#{test_case}', lst_1)