function solution(n) {
    var answer = [];
    num = String(n)

    for (let i=num.length-1; i>-1; i--){
        answer.push(Number(num.substr(i, 1)))
    }
    return answer;
}