import heapq

n = int(input())
cards = []

for _ in range(n):
  heapq.heappush(cards, int(input()))

result = 0
while len(cards) > 1:
  # 가장 작은 카드 뽑기
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  sum_value = a + b

  result += sum_value
  heapq.heappush(cards, sum_value)
  

print(result)