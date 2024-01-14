# 물이 고이기 위해서는 자신보다 더 높은 블록으로 왼쪽과 오른쪽이 둘러싸여 있어야 한다
# 이 때 물이 고이는 양은 왼쪽과 오른쪽 블록 중 더 낮은 블록과 현 위치의 값이다

h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    # 왼쪽과 오른쪽 중에서 가장 큰 걸 구해서
    left_max = max(world[:i])
    right_max = max(world[i+1:])
    # 그 둘 중에 작은 
    compare = min(left_max, right_max)
    
    # 보다 현재 위치가 작다면 그 차이만큼 빗물이 고인다
    if world[i] < compare:
        ans += compare - world[i]

print(ans)