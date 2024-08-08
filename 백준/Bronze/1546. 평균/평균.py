N = int(input())
scores = list(map(int, input().split()))
maxV = max(scores)
sumV = sum(scores)

print((sumV/maxV*100)/N)