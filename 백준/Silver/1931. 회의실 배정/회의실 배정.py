N = int(input())
lst = []
for _ in range(N):
  lst.append(list(map(int, input().split())))


lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])

result = [lst[0]]
for i in range(1, N):
  if result[-1][1] <= lst[i][0]:
    result.append(lst[i])

print(len(result))