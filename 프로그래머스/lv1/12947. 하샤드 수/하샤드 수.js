function solution(x) {
    var answer = true;
    var sum = 0;
    var numberArray = x.toString().split('').map(Number);
    numberArray.forEach((num) => {
        sum += num;
    })
    if (x % sum === 0){
        answer = true
    } else {
        answer = false
    }
    return answer;
}