/*
xor
T: O(N)
S: O(1)

Runtime: 118 ms, faster than 42.39% of C# online submissions for Single Element in a Sorted Array.
Memory Usage: 46 MB, less than 39.13% of C# online submissions for Single Element in a Sorted Array.
*/
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        int ans = 0;
        foreach (var x in nums) {
            ans ^= x;
        }
        return ans;
    }
}

/*
binary search

Runtime: 106 ms, faster than 82.61% of C# online submissions for Single Element in a Sorted Array.
Memory Usage: 45.6 MB, less than 82.61% of C# online submissions for Single Element in a Sorted Array.
*/
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        int n = nums.Length;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = ((r - l) >> 1) + l;
            if ((mid & 1) == 1) {
                mid--;
            }
            if (mid + 1 < n && nums[mid] == nums[mid + 1]) {
                l = mid + 2;
            } else if (mid - 1 >= 0 && nums[mid - 1] == nums[mid]) {
                r = mid - 2;
            } else {
                return nums[mid];
            }
        }
        return nums[l];
    }
}
