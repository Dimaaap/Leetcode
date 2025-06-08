let twoSum = (nums, target) =>{
    let seen = {}

    for(let i = 0; i < nums.length; i++){
        let diff = target - nums[i]
        if (nums[i] in seen){
            return [seen[nums[i]], i]
        } 
        
        else {
            seen[diff] = i
        }
    }

    return "Never"
}


console.log(twoSum([2, 7, 11, 15], 9))
console.log(twoSum([3, 2, 4], 6))
console.log(twoSum([3, 3], 6))