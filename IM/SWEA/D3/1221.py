T = int(input())
for test_case in range(1, T + 1):
    planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num, m = map(str, input().split())  # 테스트 케이스 번호, 길이

    numbers = list(map(str, input().split()))
    cnt_lst = [0] * 10

    # 몇 개 있는지 세주기
    for i in range(10):
        cnt_lst[i] = numbers.count(planet[i])

    # 개수 곱해서 출력하기
    print(num)
    for i in range(10):
        print(cnt_lst[i] * (planet[i] + ' '), end='')
    print()


