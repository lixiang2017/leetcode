/*
Hash Table
T: O(2N)
S: O(2N)

执行用时：16 ms, 在所有 C++ 提交中击败了33.96% 的用户
内存消耗：15.5 MB, 在所有 C++ 提交中击败了24.50% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        unordered_map<int, int> freq;
        for (int i = 0; i < nums.size(); ++i) {
            freq[nums[i]]++;
        }
        for (auto f: freq) {
            if (f.second > nums.size() / 3) {
                ans.push_back(f.first);
            }
        }
        return ans;
    }
};
