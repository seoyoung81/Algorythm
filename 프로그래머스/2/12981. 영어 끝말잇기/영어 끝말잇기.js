function solution(n, words) {
    var answer = [];
    var words_lst = [words[0]];

    for (let i=1; i<words.length; i++) {
        let a = words[i-1].length
        if (words_lst.includes(words[i]) || words[i-1][a-1] != words[i][0]) {
            let player = (i%n)+1;
            let team = Math.floor(i/n)+1;
            answer = [player, team];
            break
        }
        words_lst.push(words[i]);
        if (answer.length == 0){
            answer = [0, 0]
        }
            
    }

    return answer;
}