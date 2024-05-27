function solution(brown, yellow) {
    let answer = [];
    for (let i = 1; i < (brown - 4) / 2; i++) {
        if (i * ((brown - 4) / 2 - i) === yellow) {
            answer.push(i + 2);
            answer.push(((brown - 4) / 2 - i) + 2);
            break;
        }
    }
    answer.sort((a, b) => b - a);
    return answer;
}
