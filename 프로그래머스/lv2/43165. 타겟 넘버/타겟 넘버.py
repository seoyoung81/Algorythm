def solution(numbers, target):
    answer = 0
    nodes = [0]
    
    for num in numbers:
        temp = []
        
        for node in nodes:
            # 더한 거 담기
            temp.append(node + num)
            # 뺀 거 담기
            temp.append(node - num)
        # 새로운 계산 결과로 바꿔주기
        nodes = temp
    
    # 전체 검색
    for node in nodes:
        if node == target:
            answer += 1
    return answer