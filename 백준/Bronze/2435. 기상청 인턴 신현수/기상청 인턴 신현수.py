N, K = map(int, input().split())    # 온도를 측정한 전체 날짜의 수, 합을 구하기 위한 연속적인 날짜의 수
sequence = list(map(int, input().split()))

result = []
# k = 2
for i in range(N-K+1):
    result.append(sum(sequence[i:i+K]))

print(max(result))

