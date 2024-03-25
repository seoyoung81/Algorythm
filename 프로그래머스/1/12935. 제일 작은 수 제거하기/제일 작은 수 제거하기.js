function solution(arr) {
    var answer = [];
    
    if (arr.length <= 1) {
        return [-1]
    } else {
        const minV = Math.min(...arr)
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] !== minV) {
                answer.push(arr[i])
            }
        }
    }
    
    return answer;
}