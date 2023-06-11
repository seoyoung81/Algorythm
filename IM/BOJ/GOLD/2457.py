import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    # 1월 1일 -> 101
    a, b, c, d = map(int, sys.stdin.readline().split())
    arr.append([a * 100 + b, c * 100 + d])

# 꽃이 피는 날짜, 꽃이 지는 날짜순으로 정렬
arr.sort()

# 정원의 마지막 꽃이 지는 날짜
end = 301

# 심은 꽃의 개수
cnt = 0

# 더 이상 확인할 꽃이 없을때까지
while (arr):

    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜가 끊긴 경우
    if (end >= 1201 or arr[0][0] > end):
        break

    # 꽃이 피는 날짜가 3월 1일 이전일 때, 가장 느리게 지는 꽃의 날짜
    temp = -1

    for _ in range(len(arr)):

        # 꽃이 피는 날짜가 3월 1일 이전이라면,
        if (arr[0][0] <= end):
            # 그 중 가장 느리게 지는 꽃의 날짜를 확인
            if (temp <= arr[0][1]):
                temp = arr[0][1]

            # 확인했으면 삭제
            arr.remove(arr[0])

        else:
            break

    # 가장 꽃이 느리게 지는 날짜를 temp로 할당
    end = temp
    # 심은 꽃의 개수 증가
    cnt += 1

# 마지막으로 확인한 꽃의 지는 날짜가 12월 1일 보다 작으면, 
if end < 1201:
    print(0)
else:
    print(cnt)