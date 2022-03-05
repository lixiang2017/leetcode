/*
执行用时：8 ms, 在所有 C++ 提交中击败了21.93% 的用户
内存消耗：11.7 MB, 在所有 C++ 提交中击败了72.90% 的用户
通过测试用例：265 / 265
*/


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        next_permutation(nums.begin(), nums.end());
    }
};
