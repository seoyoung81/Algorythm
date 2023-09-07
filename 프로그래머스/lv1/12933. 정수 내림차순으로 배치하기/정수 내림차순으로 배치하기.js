function solution(n) {
    var answer = '';
    const arr = [...String(n)];
    Array.isArray(arr);
    const numArr = arr.map(Number);
    numArr.sort(function(a, b) { // 내림차순
        return b - a;
    });
    answer = Number(numArr.join(""));
 
    
    return answer;
}