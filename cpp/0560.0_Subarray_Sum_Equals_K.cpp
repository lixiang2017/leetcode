/*
Brute Force
Time: O(N^2)
Space: O(1)

85 / 89 个通过测试用例
状态：超出时间限制
提交时间：几秒前
*/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        for (int end = 0; end < nums.size(); ++end) {
            int total = 0;
            for (int start = end; start >= 0; --start) {
                total += nums[start];
                if (total == k) {
                    count += 1;
                }
            }
        }
        return count;
    }
};



/*
approach: Prefix Sum + Hash Table (Two Sum)
Time: O(N)
Space: O(N)

执行用时：68 ms, 在所有 C++ 提交中击败了99.54%的用户
内存消耗：35.1 MB, 在所有 C++ 提交中击败了93.40%的用户
*/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0, pre = 0;
        unordered_map<int, int> mp;
        mp[0] = 1;

        for (auto x: nums) {
            pre += x;
            if (mp.find(pre - k) != mp.end()) {
                count += mp[pre - k];
            }
            mp[pre]++;
        }
        return count;
    }
};


/*
prefix sum + hash table
T: O(N)
S: O(N)
执行用时：60 ms, 在所有 C++ 提交中击败了86.24% 的用户
内存消耗：36.3 MB, 在所有 C++ 提交中击败了39.61% 的用户
通过测试用例：90 / 90
*/
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> precnt = {make_pair(0, 1)};
        int ans = 0, presum = 0;
        for (int x: nums) {
            presum += x;
            if (precnt.find(presum - k) != precnt.end()) {
                ans += precnt[presum - k];
            }
            precnt[presum] += 1;
        }
        return ans;
    }
};
