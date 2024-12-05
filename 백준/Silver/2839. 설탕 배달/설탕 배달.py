N = int(input())

# 5kg 봉지를 최대한 사용
bags = 0
while N >= 0:
    # N이 5의 배수라면 (최대한 5kg 봉지를 사용)
    if N % 5 == 0:
        bags += N // 5
        print(bags)
        break
    # 그렇지 않다면 3kg 봉지 하나 사용
    N -= 3
    bags += 1
else:
    # 정확히 N kg을 만들 수 없는 경우
    print(-1)
