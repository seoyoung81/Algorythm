N = int(input())
for _ in range(N):
    S = int(input())
    i = 2
    result = True
    
    # 모든 소인수가 10^6보다만 크면 된다-> 10^6보다 큰 수는 나눴을 때 나머지가 0이어도 큰 소수라고 친다.
    while i <= 10**6:
        if S % i == 0:
            result = False
            break
        i += 1

    if result == True:
        print("YES")
    else:
        print("NO")