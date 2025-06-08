let isPalindrome = x => {
    if(x < 0){
        return false;
    }

    let newX = x; 
    let res = 0;

    while(x){
        let rest = undefined
        rest = x % 10;
        x = Math.floor(x / 10)
        res = res * 10 + rest;
    }
    return newX === res
}


console.log(isPalindrome(121))
console.log(isPalindrome(-121))
console.log(isPalindrome(10))