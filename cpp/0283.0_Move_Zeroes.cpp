/*
Runtime: 52 ms, faster than 8.68% of C++ online submissions for Move Zeroes.
Memory Usage: 19.2 MB, less than 39.59% of C++ online submissions for Move Zeroes.
*/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
            if (nums[cur] != 0) {
                swap(nums[lastNonZeroFoundAt++], nums[cur]);
            }
        }
    }
};
