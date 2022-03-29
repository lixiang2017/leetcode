/*
T: O(logN)
S: O(1)

Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Search.
Memory Usage: 54.3 MB, less than 51.69% of Java online submissions for Binary Search.
*/

class Solution {
    public int search(int[] nums, int target) {
        int pivot, left = 0, right = nums.length - 1;
        while (left <= right) {
            pivot = left + (right - left) / 2;
            if (nums[pivot] == target) return pivot;
            if (target < nums[pivot]) right = pivot - 1;
            else left = pivot + 1;
        }   
        return -1;
    }
}
