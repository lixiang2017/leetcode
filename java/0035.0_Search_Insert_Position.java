/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Search Insert Position.
Memory Usage: 41.7 MB, less than 73.75% of Java online submissions for Search Insert Position.
*/
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
                right = mid - 1; 
            } else {
                left = mid + 1;
            }
        }
        return right + 1;
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Search Insert Position.
Memory Usage: 41.8 MB, less than 73.75% of Java online submissions for Search Insert Position.
*/
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
                right = mid - 1; 
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
