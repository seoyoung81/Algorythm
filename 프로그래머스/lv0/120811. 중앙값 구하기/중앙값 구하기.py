def solution(array):
    array.sort()
    m = len(array) // 2
    answer = array[m]
    return answer