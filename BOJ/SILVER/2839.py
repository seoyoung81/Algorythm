N = int(input())    # 배달해야 하는 설탕

# 3X + 5Y = N -> X + Y의 최솟값 구하기

m = N // 5  # 5킬로그램 봉지 개수

if N % 5 == 0:  # 5로 나눠지면
    print(m)
elif N % 5 == 1:    # 나머지 1 -> 나머지 6
    if N >= 6:
        print(m+1)
    else:
        print(-1)
elif N % 5 == 2:    # 나머지 2 - > 나머지 7 -> 나머지 12
    if N >= 12:
        print(m+2)
    else:
        print(-1)
elif N % 5 == 3:    # 나머지 3
    print(m+1)
elif N % 5 == 4:    # 나머지 4 -> 나머지 9
    if N >= 9:
        print(m+2)
    else:
        print(-1)