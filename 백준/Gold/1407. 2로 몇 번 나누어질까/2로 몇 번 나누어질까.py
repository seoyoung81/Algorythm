def power_count(n):
    if n % 2 == 1:
        return n // 2 + 2 * power_count(n // 2) + 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n // 2 + 2 * power_count(n // 2)


A, B = map(int, input().split())
print(power_count(B)-power_count(A-1))