def prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

N = str(input())
number = []
for num in N:
    number.append(int(num))

# 1번 숫자인지 판단하기
if any(num in [3, 4, 7] for num in number):
    print("no")
else:
    # 2번 원래 수가 소수인지 판단하기
    if not prime(int(N)):
        print("no")
    else:
        # 3번 뒤집은 수가 소수인지 판단하기
        # 먼저 뒤집기
        for i in range(len(number)):
            if number[i] == 6:
                number[i] = 9
            elif number[i] == 9:
                number[i] = 6
        last_number = ''
        for i in range(len(number)-1, -1, -1):
            last_number += str(number[i])
        if not prime(int(last_number)):
            print("no")
        else:
            print("yes")