const uniquePaths = (m, n) => {
    if(m === 1 && n === 1){
        return 1;
    }
    if(m === 0 || n === 0){
        return 0;
    }

    return(uniquePaths(m, n - 1) + uniquePaths(m - 1, n))
}

console.log(uniquePaths(3, 7))
console.log(uniquePaths(3, 2))