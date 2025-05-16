let numberOfPairs = function(nums1, nums2, k){
    let counter = 0;
    
    for(let i of nums1){
        for(let j of nums2){
            let prod = j * k
            if(i % prod === 0){
                counter++;
            }
        }
    }
    return counter
}

console.log(numberOfPairs([1, 3, 4], [1, 3, 4], 1))
console.log(numberOfPairs([1, 2, 4, 12], [2, 4], 3))