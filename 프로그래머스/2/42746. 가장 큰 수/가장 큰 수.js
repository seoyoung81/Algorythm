function solution(numbers) {
    var answer = '';
    numbers_ = numbers.map(String);
    numbers_.sort((a, b) => (b+a) - (a+b))
    
    if (numbers_[0] === '0') {
        return '0';
    }
    
    answer = numbers_.join('');
    
    return answer;
}