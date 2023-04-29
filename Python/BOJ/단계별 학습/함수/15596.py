def ans(a):
    ans = 0
    for i in a:
        ans += i
    return ans





a = map(int, input().split())
print(ans(a))