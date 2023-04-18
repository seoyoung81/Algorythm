# 에라토스테네스의 체
'''
1. 전체 수 만큼 True 리스트 생성
2. 2부터 +1 씩 해주면서 배수라면 Flase로 바꾸기
-> 소수만 True
'''
from sys import stdin

arr = [True for i in range(1000001)]

for i in range(2, 1001):
    if arr[i] == True:
        for j in range(i+i, 1000001, i):
            arr[j] = False

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    for i in range(3, len(arr)):
        if arr[i] == True:
            if arr[n-i] == True:
                print(f'{n} = {i} + {n-i}')
                break