N = int(input())
number = list(map(int, input().split()))

count = 0
for num in number:
    if num == 1:
        pass
    else:
        prime = []
        for i in range(2, num+1):
            if num % i == 0:
                prime.append(i)
            if len(prime) > 1:
                break

        if len(prime) == 1:
            count += 1

print(count)