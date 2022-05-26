/*
执行用时：8 ms, 在所有 C++ 提交中击败了92.45% 的用户
内存消耗：10.1 MB, 在所有 C++ 提交中击败了85.67% 的用户
通过测试用例：54 / 54
*/
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> ans;
        for (auto &n: nums) {
            auto i = lower_bound(ans.begin(), ans.end(), n);
            if (i == ans.end()) {
                ans.push_back(n);
            } else {
                ans[i - ans.begin()] = n;
            }
        }
        return ans.size();
    }
};



/*
Runtime: 22 ms, faster than 69.89% of C++ online submissions for Longest Increasing Subsequence.
Memory Usage: 10.5 MB, less than 67.17% of C++ online submissions for Longest Increasing Subsequence.
*/
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> f;
        for (auto x: nums) {
            if (f.size() == 0 || x > f.back()) {
                f.push_back(x);
            } else {
                auto it = lower_bound(f.begin(), f.end(), x);
                f[it - f.begin()] = x;
            }
        }
        return f.size();
    }
};
