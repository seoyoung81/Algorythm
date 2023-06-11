# from itertools import combinations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     left, right = map(int, input().split())
#     arr = [i for i in range(right)]
#
#     print(len(list(combinations(arr, left))))

import math
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(bridge)