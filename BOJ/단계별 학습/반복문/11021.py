
testcase = int(input())

for i in range(1, testcase+1):
    A, B = map(int, input().split())    # a,b 가 하나가 아니고 반복되는 것이므로 for 문 안에 넣어줘야함
    print(f'Case #{i}: {A+B}')
