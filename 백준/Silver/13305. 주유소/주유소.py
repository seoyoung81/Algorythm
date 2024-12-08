n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
cost = price[0]
result = distance[0] * price[0]

for i in range(1, n-1):
  cost = min(cost, price[i])
  result += cost * distance[i]

print(result)