/*
执行用时：12 ms, 在所有 C++ 提交中击败了36.76% 的用户
内存消耗：15.6 MB, 在所有 C++ 提交中击败了96.45% 的用户
通过测试用例：285 / 285
*/
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        partition(nums.begin(), nums.end(), [&](int x) {
            return (x & 1) == 0;
        });
        return nums;
    }
};


/*
执行用时：8 ms, 在所有 C++ 提交中击败了72.75% 的用户
内存消耗：15.8 MB, 在所有 C++ 提交中击败了60.21% 的用户
通过测试用例：285 / 285
*/
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        partition(nums.begin(), nums.end(), [&](int x) {
            return (x % 2) == 0;
        });
        return nums;
    }
};


/*
执行用时：4 ms, 在所有 C++ 提交中击败了96.19% 的用户
内存消耗：15.8 MB, 在所有 C++ 提交中击败了67.04% 的用户
通过测试用例：285 / 285
*/
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        stable_partition(nums.begin(), nums.end(), [&](int x) {
            return (x % 2) == 0;
        });
        return nums;
    }
};
