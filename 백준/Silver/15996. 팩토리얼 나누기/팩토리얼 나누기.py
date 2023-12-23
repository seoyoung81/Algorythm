N, A = map(int, input().split())    # 정수, 소수
M = N // A # A 의 배수의 개수
count = M

for i in range(2, 31):
    if N // A**i >= 1:
        count += N // A**i
    else:
        break
print(count)

'''
5 // 2 = 2 -> 1부터 5까지 2의 배수가 2개임
M = 2 -> 최소 2가 2개는 들어갈 수 있음
첫번째 -> 2**2가 몇개 들어가는지 확인해야됨
두번째 -> 2**3가 몇개 들어가는지 확인해야됨
'''

