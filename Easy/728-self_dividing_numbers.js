let selfDividingNumbers = function(left, right){
    
    let result = []
    
    for(let i = left; i < right + 1; i++){
        if(isNumberSelfDividing(i)){
            result.push(i);
        }
    }

    return result;
}

let isNumberSelfDividing = function(number){
    let numberStr = number.toString();

    for(let i of numberStr){
        let digit = parseInt(i, 10);
        if(number % digit !== 0){
            return false
        }
    }
    return true
}

console.log(selfDividingNumbers(1, 22))
console.log(selfDividingNumbers(47, 85))