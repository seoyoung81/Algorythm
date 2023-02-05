A, B, C = map(int, input().split())

# A = 1000(고정비용), B = 70(인건비, 재료비), C = 노트북 가격
# n = 몇 대 팔았는지

for n in range(2100000000):
    sell_cost = A + B * n       # 총 생산비용
    all_cost = sell_cost - C    # 총 판매비용

    if 0 < all_cost:
        print(all_cost)
        break