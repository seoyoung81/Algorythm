# 순열을 직접 만들어보자
def perm(i, k):
	if i==k:
		print(p)
	else:
		for j in range(k):
			if used[j] == 0:
				p[i] = A[j]
				used[j] = 1
				perm(i+1, k)
				used[j] = 0




A = [0, 0, 1, 1]
p = [0] * 4
used = [0] * 4
perm(0, 4)






# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())    # N x N arr
#     # arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 오른쪽으로 갈 지 왼쪽으로 갈지 선택하기
#     # 총 이동 횟수 -> (N-1) * 2
#     n = (N-1) * 2
#
#     result_lst = []
#     '''
#     for i in range(1 << n):  # 1<<n : 부분집합의 개수 (0, 2**n - 1)
#         move = []
#         for j in range(n):  # 원소의 수만큼 비트를 비교함
#             if i & (1 << j):  # i의 j번 비트가 1인 경우
#                 move.append(1)
#             else:
#                 move.append(0)
#     '''
#         # print(move)
#     # move 다시 구해보기!
#     move =
#     print(move)





    #         result = arr[0][0]
    #         p = [0]
    #         q = [0]
    #         for step in move:
    #             if step == 0:   # 0이면 오른쪽으로 가기
    #                 np, nq = p[-1], q[-1]+1
    #                 if 0 <= np < N and 0 <= nq < N:
    #                     result += arr[np][nq]
    #                     q.append(nq)
    #
    #             else:   # 1이면 아래로 가기
    #                 np, nq = p[-1] + 1 , q[-1]
    #                 if 0 <= np < N and 0 <= nq < N:
    #                     result += arr[np][nq]
    #                     p.append(np)
    #         result_lst.append(result)
    # print(f'#{test_case}', min(result_lst))