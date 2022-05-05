/*
双指针，双向奔赴

执行用时：20 ms, 在所有 C++ 提交中击败了94.43% 的用户
内存消耗：25.3 MB, 在所有 C++ 提交中击败了41.76% 的用户
通过测试用例：137 / 137
*/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        int l = 0, r = n - 1, i = n - 1;
        while (l <= r) {
            if (abs(nums[l]) < abs(nums[r])) {
                ans[i] = nums[r] * nums[r];
                r--;
            } else {
                ans[i] = nums[l] * nums[l];
                l++;
            }
            i--;
        }
        return ans;
    }
};

