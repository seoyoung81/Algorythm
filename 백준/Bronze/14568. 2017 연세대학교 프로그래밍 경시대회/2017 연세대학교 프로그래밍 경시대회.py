N = int(input())

# 남규 = 영훈+2이상
# 0개는 아무도 없음
# 택화 % 2 != 0
count = 0
if N>=4:
    for i in range(1, N-2):
        for j in range(i+2, N-1-i):
            k = N-(i+j)

            if k>0 and k%2==0:
                count += 1
else:
    count = 0

print(count)