/*
Runtime: 42 ms, faster than 14.29% of C++ online submissions for Product of Array Except Self.
Memory Usage: 24 MB, less than 80.14% of C++ online submissions for Product of Array Except Self.
*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l = 1, r = 1, n = nums.size();
        vector<int> ans(n, 1);
        for (int i = 0; i < n; ++i) {
            ans[i] *= l;
            ans[n - 1 - i] *= r;
            l *= nums[i];
            r *= nums[n - 1 - i];
        }
        return ans;
    }
};
