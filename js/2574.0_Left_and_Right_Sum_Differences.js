/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {
    const total = _.sum(nums);
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        nums[i] = Math.abs(leftSum * 2 + x - total);
        leftSum += x;
    }
    return nums;
};