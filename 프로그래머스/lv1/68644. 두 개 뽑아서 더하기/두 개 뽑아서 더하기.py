def solution(numbers):
    answer = []
    m = len(numbers)
    for i in range(m-1):
        for j in range(i+1, m):
            if not numbers[i]+numbers[j] in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer