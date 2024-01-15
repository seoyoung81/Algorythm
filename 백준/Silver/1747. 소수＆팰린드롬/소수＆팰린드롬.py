import sys
input = sys.stdin.readline

n = int(input())

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

result = 0
for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if is_prime(i) == True:
            result = i
            break
if result == 0:
    result = 1003001
    
print(result)

