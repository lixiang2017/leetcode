/*
DP
Time: O(N)
Space: O(1)

执行用时：24 ms, 在所有 C++ 提交中击败了66.42% 的用户
内存消耗：22.4 MB, 在所有 C++ 提交中击败了46.23% 的用户
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maximum = nums[0], pre = 0;
        for (auto num: nums) {
            pre = max(pre + num, num);
            maximum = max(maximum, pre);
        }
        return maximum;
    }
};
