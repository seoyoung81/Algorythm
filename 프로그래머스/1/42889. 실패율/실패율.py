def solution(N, stages):
    # N 전체 스테이지의 개수
    # stages 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
    # 실패율이 높은 스테이지부터 내림차순으로 출력
    # 실패율 = 스테이지에 도달했지만 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
    answer = []
    
    for i in range(1, N+1):
        a = 0
        b = 0
        for num in stages:
            if num == i:
                b += 1
                a += 1
            elif num > i:
                a += 1
        if a == 0:
            answer.append([0, i])
        else:
            answer.append([round(b/a, 15), i])
            
    answer = sorted(answer, key=lambda x: x[0], reverse=True)
    answer = [lst[1] for lst in answer]
  
    return answer