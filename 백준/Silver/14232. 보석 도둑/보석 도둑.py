k = int(input())

# 소인수분해하
lis = []
mod = 2
while k != 1:
    if mod > 1000000:
        lis.append(k)
        break

    if k % mod == 0:
        k //= mod
        lis.append(mod)
    else:
        mod += 1

print(len(lis))
print(*lis)

