from collections import deque


N = int(input())
card = deque()
for i in range(1, N+1):
    card.append(i)

while len(card) != 1:
    card.popleft()  # 가장 첫번째 원소 버리고
    card.append(card.popleft())     # 첫번째 원소가 된 두번째 원소를 뒤에 추가


print(card[0])