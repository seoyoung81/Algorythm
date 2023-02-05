# 일단 포기.. 
# N번 정류장
# K: 한 번 충전으로 최대한 이동할 수 있는 정류장 수
# 충전기가 설치된 M개의 정류장 번호 제공
# 최소한 몇 번의 충전을 해야 도착할 수 있는가 -> 도착할 수 없는 경우 0을 출력

T = int(input())    # 노선수 = 케이스 수

'''
예시
3
3 10 5
1 3 5 7 9
1에서 하면 5까지 못감, 3. 5. 7. 3번
'''
count = 0
for i in range(T):
    K, N, M = map(int, input().split())     # 최대 이동, 정류장 개수, 충전기 개수
    M_number = list(map(int, input().split()))     # 충전기가 설치된 정류장 수
    # print(M_number)   # [0 1 3 5 7 9 10]
    M_number.insert(0, 0)
    M_number.append(N)
    print(M_number)
    for j in range(M):
        # print(M_number[j])
        # print(M_number[j+1] - M_number[j])
        if M_number[j+1] - M_number[j] > K:
            print(f'#{i+1} 0')
            break

        if M_number[j+1] - M_number[j] == K:
            count += 1
        print(count)
        if M_number[j+1] - M_number[j] < K and M_number[j+2] - M_number[j] >= K:
            count += 1
        print(count)
    if M_number[-1] - M_number[-2] == K:
        count += 1
        print(count)
    print(f'#{i+1} {count}')