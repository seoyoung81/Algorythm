N = int(input())
rope = []
for _ in range(N):
  rope.append(int(input()))

rope.sort()

answer = []
for x in rope:
  answer.append(x*N)
  N -= 1

print(max(answer))
