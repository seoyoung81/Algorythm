N, M = map(int, input().split())    # N 듣도 못한 사람 M 보도 못한 사람
n = []
m = []
for _ in range(N):
    n.append(str(input()))
for _ in range(M):
    m.append(str(input()))

# 교집합 구하기
intersection = list(set(n) & set(m))
print(len(intersection))

intersection.sort()
for i in range(len(intersection)):
    print(intersection[i])
