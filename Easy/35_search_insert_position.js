let searchInsert = (nums, target) => {
    let [left, right] = [0, nums.length - 1];

    while(left <= right){
        mid = Math.floor((left + right) / 2)

        if(nums[mid] === target){
            return mid
        } else if(nums[mid] > target){
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return left;
}

console.log(searchInsert([1, 3, 5, 6], 5))
console.log(searchInsert([1, 3, 5, 6], 2))
console.log(searchInsert([1, 3, 5, 6], 7))