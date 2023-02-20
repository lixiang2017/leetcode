/*
Runtime: 74 ms, faster than 23.53% of JavaScript online submissions for Search Insert Position.
Memory Usage: 42 MB, less than 64.99% of JavaScript online submissions for Search Insert Position.
*/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        let mid = ((right - left) >> 1) + left;
        if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    return right + 1;     
};


/*
Runtime: 66 ms, faster than 56.02% of JavaScript online submissions for Search Insert Position.
Memory Usage: 42.1 MB, less than 44.97% of JavaScript online submissions for Search Insert Position.
*/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        let mid = ((right - left) >> 1) + left;
        if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    return left;     
};
