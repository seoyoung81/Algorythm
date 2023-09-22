def solution(n, m, section):
    # 벽 길이 n 미터
    # 롤러 길이 m 미터
    # section 칠해야 하는 곳
    answer = 1
    paint = section[0]
    
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
   
      
    return answer