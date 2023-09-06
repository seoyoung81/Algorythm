function solution(s){

    const arr = [...s];
    let alpha1 = 0;
    let alpha2 = 0;
    
    Array.isArray(arr);
    arr.forEach((char) => {
        if (char === 'P' || char === 'p'){
            alpha1++;
        } else if (char === 'Y' || char === 'y'){
            alpha2++;
        }
    })
    
    if (alpha1 === alpha2){
        return true
    } else {
        return false
    }
    
}