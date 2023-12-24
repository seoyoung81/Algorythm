N = int(input())    # 테스트 케이스의 개수

# 최대 공약수 구하기
def greatestCommonDivisor(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

for test_case in range(N):
    number = list(map(int, input().split()))
    m = len(number)
    result = 0
    for i in range(m-1):
        for j in range(i+1, m):
            gcd = greatestCommonDivisor(number[i], number[j])
            if result < gcd:
                result = gcd
    print(result)