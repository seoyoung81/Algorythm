function solution(arr, divisor) {
    var answer = [];
    arr.sort((a, b) => a - b)
    
    arr.forEach((num) => {
        if (num % divisor === 0) {
            answer.push(num)
        }
    })
    
    if (answer.length === 0) {
        answer = [-1]
    }
    
    return answer;
}