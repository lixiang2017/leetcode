/*
执行用时：8 ms, 在所有 C++ 提交中击败了92.05% 的用户
内存消耗：10.5 MB, 在所有 C++ 提交中击败了38.27% 的用户
通过测试用例：57 / 57
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (um.count(target - nums[i]) > 0) {
                auto it = um.find(target - nums[i]);
                return {it->second, i};
            }
            um.insert({nums[i], i});
        }
        return {-1, -1};
    }
};


/*
执行用时：12 ms, 在所有 C++ 提交中击败了64.55% 的用户
内存消耗：10.4 MB, 在所有 C++ 提交中击败了52.98% 的用户
通过测试用例：57 / 57
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> um;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            auto it = um.find(target - nums[i]);
            if (it != um.end()) {
                return {it->second, i};
            }
            um.insert(pair<int, int>(nums[i], i));
        }
        return {};
    }
};

