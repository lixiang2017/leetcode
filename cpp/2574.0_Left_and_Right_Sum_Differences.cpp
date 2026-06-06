class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int total = reduce(nums.begin(), nums.end());
        int left_sum = 0;
        for (int& x: nums) {
            left_sum += x;
            x = abs(left_sum * 2 - x - total);
        }    
        return nums;
    }
};