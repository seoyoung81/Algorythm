def solution(lines):
    ##### 다시 풀기
    table = [set([]) for _ in range(200)] # -100~100
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) 

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1

    return answer