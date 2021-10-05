/*
xor

执行用时：8 ms, 在所有 C++ 提交中击败了98.60% 的用户
内存消耗：16.7 MB, 在所有 C++ 提交中击败了70.18% 的用户
通过测试用例：122 / 122
*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            res ^= i ^ nums[i];
        }
        res ^= nums.size();
        return res;
    }
};



/*
执行用时：12 ms, 在所有 C++ 提交中击败了91.12% 的用户
内存消耗：16.8 MB, 在所有 C++ 提交中击败了31.98% 的用户
通过测试用例：122 / 122
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0, len = nums.size();
        int predictSum = (len + 1) * len / 2;
        for (int num: nums)
            sum += num;
        return predictSum - sum;
    }
};

