/*
JavaScript
60 ms
42.1 MB
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var findTheArrayConcVal = function(nums) {
    let ans = 0;
    for (let i = 0, j = nums.length - 1; i <= j; i++, j--) {
        if (i < j) {
            ans += parseInt(nums[i].toString() + nums[j].toString());
        } else {
            ans += nums[i];
        }
    }
    return ans
};
