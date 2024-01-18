import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Aarr = list(map(int, input().split()))
Barr = list(map(int, input().split()))


Carr = Aarr + Barr
print(*sorted(Carr))





