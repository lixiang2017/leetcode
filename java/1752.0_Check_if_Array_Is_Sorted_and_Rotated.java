/*
approach: One Pass
Time: O(N)
Space: O(1)

Runtime: 0 ms, faster than 100.00% of Java online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 36.1 MB, less than 97.46% of Java online submissions for Check if Array Is Sorted and Rotated.
*/

class Solution {
    public boolean check(int[] nums) {
        int k = 0, N = nums.length;
        for (int i = 0; i < N; i++) {
            if (nums[i] > nums[(i + 1) % N]) {
                k += 1;
            }
            if (k > 1) {
                return false;
            }
        }
        return true;
    }
}
