/*
T: O(logN)
S: O(1)

Runtime: 78 ms, faster than 68.45% of JavaScript online submissions for Binary Search.
Memory Usage: 45.7 MB, less than 7.01% of JavaScript online submissions for Binary Search.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        if (nums[middle] > target) {
            right = middle - 1;
        } else if (nums[middle] < target) {
            left = middle + 1;
        } else {
            return middle;
        }
    }
    return -1;
};
