/*
approach: One Pass
Time: O(N)
Space: O(1)

Runtime: 4 ms, faster than 47.34% of C++ online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 8.5 MB, less than 10.28% of C++ online submissions for Check if Array Is Sorted and Rotated.
*/

class Solution {
public:
    bool check(vector<int>& nums) {
        int N = nums.size();
        for (int i = 0, k = 0; i < N; i++) {
            if (nums[i] > nums[(i + 1) % N] && ++k > 1)
                return false;
        }
        return true;
    }
};
