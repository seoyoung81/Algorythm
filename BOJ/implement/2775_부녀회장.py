T = int(input())    # test_case
for test_case in range(1, T+1):
    k = int(input())    # k층 <= 14
    n = int(input())    # n호에 살고 있는 사람의 수는? <= 14


    apartment_arr = [[1] * 15 for _ in range(15)]
    apartment_arr[0] = [i for i in range(1, 15)]    # 0 층의 i호에는 i명이 산다

    # 층마다의 사람을 구해보자
    for i in range(1, 15):
        for j in range(2, 15):
            apartment_arr[i][j-1] = sum(apartment_arr[i-1][:j])
    # print(apartment_arr)

    # k층의 n호
    print(apartment_arr[k][n-1])