let containsDuplicate = (nums) => {
  let seen = new Set();

  for (let i in nums) {
    if (seen.has(nums[i])) {
      return true;
    } else {
      seen.add(nums[i]);
    }
  }
  return false;
};

console.log(containsDuplicate([1, 2, 3, 1]));
console.log(containsDuplicate([1, 2, 3, 4]));
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
