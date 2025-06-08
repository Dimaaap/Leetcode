let removeDuplicates = nums => {
    
    let seen = []
    let i = res = 0;
    while(i < nums.length){
        
        if(seen.includes(nums[i])){
            nums.splice(i, 1);
        } else {
            seen.push(nums[i]);
            res++;
            i++;
        }
    }
    return res;
}


console.log(removeDuplicates([1, 1, 2]))
console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))