/*
Hash Table

执行用时：8 ms, 在所有 C++ 提交中击败了97.44% 的用户
内存消耗：12.1 MB, 在所有 C++ 提交中击败了21.86% 的用户
通过测试用例：236 / 236
*/

class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        vector<int> cnt(100);
        for (int n: nums) {
            cnt[n - 1]++;
        }
        int ans = 0;
        for (int i = 0; i + k < 100; ++i) {
            ans += cnt[i] * cnt[i + k];
        }
        return ans;
    }
};




/*
Hash Table
使用int cnt[100] = {0};会更省内存

执行用时：8 ms, 在所有 C++ 提交中击败了97.44% 的用户
内存消耗：12 MB, 在所有 C++ 提交中击败了73.63% 的用户
通过测试用例：236 / 236
*/
class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        // vector<int> cnt(100);
        int cnt[100] = {0};
        for (int n: nums) {
            cnt[n - 1]++;
        }
        int ans = 0;
        for (int i = 0; i + k < 100; ++i) {
            ans += cnt[i] * cnt[i + k];
        }
        return ans;
    }
};


/*
Brute Force

执行用时：16 ms, 在所有 C++ 提交中击败了70.57% 的用户
内存消耗：12 MB, 在所有 C++ 提交中击败了64.71% 的用户
通过测试用例：236 / 236
*/
class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int ans = 0, len = nums.size();
        for (int i = 0; i < len; ++i) {
            for (int j = i + 1; j < len; ++j) {
                if (fabs(nums[i] - nums[j]) == k) ans++;
            }
        }
        return ans;
    }
};
