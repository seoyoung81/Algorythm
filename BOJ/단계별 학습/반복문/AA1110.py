N = int(input())    # 68
number = N
count = 0

while True:
    a = number // 10 # 6
    b = number % 10 # 8
    c = (a + b) % 10    # 4
    number = (b * 10) + c
    
    count += 1
    if number == N:
        break

print(count)