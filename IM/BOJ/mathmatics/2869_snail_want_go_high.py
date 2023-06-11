A, B, V = list(map(int, input().split()))   # A: 낮, B: 밤, V: 나무

n = (V-A-1) / (A-B)  # 지나간

print(round(n+1, 0))