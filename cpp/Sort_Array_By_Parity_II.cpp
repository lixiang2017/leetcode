/*
Two Pointers
T: O(N)
S: O(1)

You are here!
Your runtime beats 98.31 % of cpp submissions.
You are here!
Your memory usage beats 98.57 % of cpp submissions

i: even
j: odd
*/
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int n = nums.size();
        int j = 1;
        for (int i = 0; i < n; i += 2) {
            if (nums[i] & 1) {                 // nums[i] % 2
                while (nums[j] & 1) {
                    j += 2;
                }
                swap(nums[i], nums[j]);
            }
        }
        return nums;
    }
};
