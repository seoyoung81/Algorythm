# 재귀함수로 1부터 n 까지의 합 구하기
n = int(input())

def my_sum(n):
    if n < 2:
        return 1
    else:
        return (n + my_sum(n-1))

print(my_sum(5))