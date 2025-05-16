let countPairs = function(nums, k){
    let counter = 0;

    for(let i = 0; i < nums.length; i++){
        for(let j = i + 1; j < nums.length; j++){
            if (nums[i] === nums[j]){
                let prod = i * j;
                if(prod % k === 0){
                    counter++;
                }
            }
        }
    }

    return counter;
}

console.log(countPairs([3, 1, 2, 2, 2, 1, 3], 2))
console.log(countPairs([1, 2, 3, 4], 1))
