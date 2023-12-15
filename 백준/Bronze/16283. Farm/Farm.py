# 양 a 그램, 염소 b 그램, 전체 n마리, 소비한 사료 w 그램
a, b, n, w = map(int, input().split())

result_sheep = 0
result_goat = 0
result = 0

for i in range(1, n):
    sheep = i
    goat = n - i
    if sheep * a + goat * b == w:
        result_sheep = sheep
        result_goat = goat
        result += 1

if result != 1:
    print(-1)
else:
    print(result_sheep, result_goat)
