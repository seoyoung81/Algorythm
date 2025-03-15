function solution(citations) {
    var answer = 0; // h-index
    let n = citations.length;   // 논문의 개수
    citations.sort((a, b) => b - a);
    for (let i = 1; i <= n; i++) {
        if (citations[i-1] > i-1) answer++;
        else break
    }
    return answer;
}