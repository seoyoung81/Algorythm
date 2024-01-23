import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print("NO")
else:

    sam_numbers = [3**i for i in range(41)]
    for i in range(40, -1, -1):
        if n >= sam_numbers[i]:
            n = n - sam_numbers[i]

    if n == 0:
        print("YES")
    else:
        print("NO")

