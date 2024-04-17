function solution(phone_number) {
    var answer = '';
    len = phone_number.length;
    
    for (let i = 0; i < len; i++) {
        const num = phone_number[i]
        if (len - i <= 4) {
            answer += num
        } else {
            answer += "*"
        }
    }
    
    return answer;
}