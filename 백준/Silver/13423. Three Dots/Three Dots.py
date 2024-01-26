import sys
input = sys.stdin.readline

def bin_search(l,r,t):
    while l<=r:
        m = (l+r)//2
        if dots[m] == t:
            return 1
        if dots[m] > t:
            r = m-1
        else:
            l = m+1
    return 0

t = int(input())
for test_case in range(t):
    n = int(input())
    dots = sorted(list(map(int, input().split())))
    l, r = 0, n-1
    result = 0

    for i in range(n-1):
        for j in range(i+1, n):
            dist = abs(dots[j]-dots[i])# 두 점 사이의 거리
            if bin_search(l, r, dots[j] + dist):#target은 두점사이 거리만큼 떨어진 다른 점
                result+=1
    print(result)
