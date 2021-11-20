/*
T: O(2N)
S: O(1)

Runtime: 52 ms, faster than 70.67% of C++ online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 33.8 MB, less than 54.30% of C++ online submissions for Find All Numbers Disappeared in an Array.
*/

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (auto x: nums) {
            int idx = abs(x) - 1;
            nums[idx] = -abs(nums[idx]);
        }
        
        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) {
                ans.push_back(i + 1);
            }
        }
        return ans;
    }
};


/*
Runtime: 56 ms, faster than 58.30% of C++ online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 34.9 MB, less than 26.30% of C++ online submissions for Find All Numbers Disappeared in an Array.
*/

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> hash(n + 1, 0);
        for (auto x: nums) {
            hash[x]++;
        }
        vector<int> ans;
        for (int i = 1; i < n + 1; i++) {
            if (hash[i] == 0) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
