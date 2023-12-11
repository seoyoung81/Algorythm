N = int(input())    # 시험장의 개수
list_A = list(map(int, input().split()))    # 시험장에 있는 응시자의 수
B, C = map(int, input().split())    # 총 감독관이 감시할 수 있는 응시자수, 부감독관이 감시하 수 있는 감시자수

# 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수
# 총 감독관은 오직 1명만, 부감독관은 여러명 가능
result = N
for num in list_A:
    num -= B
    if num > 0:
        if num % C:
            result += (num // C) + 1
        else:
            result += (num // C)



print(result)

