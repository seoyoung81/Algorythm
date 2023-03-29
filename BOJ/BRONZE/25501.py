def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


T = int(input())
for _ in range(T):
    s = str(input())
    cnt = 1
    print(isPalindrome(s), cnt)