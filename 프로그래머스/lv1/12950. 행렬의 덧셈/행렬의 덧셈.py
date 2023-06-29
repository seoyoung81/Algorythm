def solution(arr1, arr2):
    answer = []
    m = len(arr1[0])
    n = len(arr1)
    
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(arr1[i][j] + arr2[i][j])
        answer.append(lst)
    return answer