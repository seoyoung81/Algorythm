// js 를 이용해서 입출력 알고리즘 문제 풀기
// node.js의 file system 모듈을 불러온다
const fs = require('fs')

// string 자료형으로 넘기는 경우
const inputData = fs.readFileSync(0, 'utf8').toString().split(' ')

const A = parseInt(inputData[0])
const B = parseInt(inputData[1])

console.log(A+B)
