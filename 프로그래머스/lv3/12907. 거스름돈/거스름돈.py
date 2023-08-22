def solution(n, money):
    answer = 0
   
    # 0, 1, 2, ... , n원 만드는 경우의 수 리스트에 쌓기
    dp = [0] * (n + 1)
    # 0원 만드는 방법은 1가지이다 
    dp[0] = 1 

    # 1, 2, 5
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
       

    answer = dp[n]
    # 제한사항
    if answer >= 1000000007:
        answer %= 1000000007
    return answer