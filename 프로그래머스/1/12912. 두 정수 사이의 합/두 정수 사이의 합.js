function solution(a, b) {
    var answer = 0;
    let _a = 0;
    let _b = 0;
    if (a <= b) {
        _a = a;
        _b = b;
    } else {
        _a = b;
        _b = a;
    }
    for (let i = _a; i <= _b; i++) { 
      answer += i
    }   
    return answer;
}