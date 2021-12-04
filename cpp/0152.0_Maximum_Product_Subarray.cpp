/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Maximum Product Subarray.
Memory Usage: 12 MB, less than 7.19% of C++ online submissions for Maximum Product Subarray.
*/

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> maxF(nums), minF(nums);
        for (int i = 1; i < nums.size(); i++) {
            maxF[i] = max(maxF[i - 1] * nums[i], max(nums[i], minF[i - 1] * nums[i]));
            minF[i] = min(maxF[i - 1] * nums[i], min(nums[i], minF[i - 1] * nums[i]));
        }
        return *max_element(maxF.begin(), maxF.end());
    }
};


/*
Runtime: 4 ms, faster than 81.49% of C++ online submissions for Maximum Product Subarray.
Memory Usage: 11.8 MB, less than 52.62% of C++ online submissions for Maximum Product Subarray.
*/
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxf = nums[0], minf = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxf, mn = minf;
            maxf = max(nums[i], max(nums[i] * mx, nums[i] * mn));
            minf = min(nums[i], min(nums[i] * mx, nums[i] * mn));
            ans = max(ans, maxf);
        }        
        return ans;
    }
};