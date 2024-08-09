alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cnt = [0] * 26

word = str(input()).lower()
for char in word:
    idx = alpa.index(char)
    cnt[idx] += 1

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(alpa[cnt.index(max(cnt))].upper())
