let removeElement = (nums, val) => {
    let i = 0;
    while(i < nums.length){
        if(nums[i] === val){
            nums.splice(i, 1);
        } else {
            i++;
        }
    }
    return nums.length
}


console.log(removeElement([3, 2, 2, 3], 3))
console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))