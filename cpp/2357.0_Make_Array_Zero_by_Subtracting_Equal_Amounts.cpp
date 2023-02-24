/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了11.43% 的用户
通过测试用例：95 / 95
*/
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        return s.size() - s.count(0);        
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.2 MB, 在所有 C++ 提交中击败了14.00% 的用户
通过测试用例：95 / 95
*/
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_map<int, int> m;
        for (int x : nums) m[x]++;
        return m.size() - m.count(0);        
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了12.57% 的用户
通过测试用例：95 / 95
*/
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> s;
        for (int x : nums) {
            if (x > 0) s.insert(x);
        }
        return s.size();        
    }
};

