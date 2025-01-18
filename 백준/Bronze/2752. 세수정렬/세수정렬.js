let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split('\n')

let data = input[0].split(' ').map(Number)

function compare (a, b) {
  return a - b
}

data.sort(compare)
console.log(data[0], data[1], data[2])
