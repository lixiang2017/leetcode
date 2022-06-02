/*
Runtime: 3 ms, faster than 76.56% of C++ online submissions for Running Sum of 1d Array.
Memory Usage: 8.6 MB, less than 37.99% of C++ online submissions for Running Sum of 1d Array.
*/
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        // initialisze answer array with first element in nums.
        vector<int> ans = {nums[0]};
        for (int i = 1; i < nums.size(); ++i) {
            // answer at index `i` is sum of answer at `i-1` and element at `i`
            ans.push_back(ans.back() + nums[i]);
        }
        return ans;
    }
};


/*
Runtime: 3 ms, faster than 76.56% of C++ online submissions for Running Sum of 1d Array.
Memory Usage: 8.4 MB, less than 75.04% of C++ online submissions for Running Sum of 1d Array.
*/
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};

