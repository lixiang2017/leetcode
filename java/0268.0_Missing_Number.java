/*
Runtime: 1 ms, faster than 65.97% of Java online submissions for Missing Number.
Memory Usage: 51.1 MB, less than 48.77% of Java online submissions for Missing Number.
*/
class Solution {
    public int missingNumber(int[] nums) {
        int diff = nums.length;
        for (int i = 0; i < nums.length; i++)
            diff += i - nums[i];
        return diff;        
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Missing Number.
Memory Usage: 51.4 MB, less than 31.43% of Java online submissions for Missing Number.
*/
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length, _sum = 0;
        for (int e: nums) {
            _sum += e;
        }
        return n * (n + 1) / 2 - _sum;
    }
}

