/*
执行用时：8 ms, 在所有 C++ 提交中击败了11.93% 的用户
内存消耗：8.7 MB, 在所有 C++ 提交中击败了8.48% 的用户
通过测试用例：63 / 63
*/

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        return max_element(nums.begin(), nums.end()) - nums.begin();
    }
};
