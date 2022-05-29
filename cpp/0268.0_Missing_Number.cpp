/*
Runtime: 22 ms, faster than 72.29% of C++ online submissions for Missing Number.
Memory Usage: 17.9 MB, less than 93.84% of C++ online submissions for Missing Number.
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), _sum = 0;
        for (int e: nums) {
            _sum += e;
        }
        return n * (n + 1) / 2 - _sum;        
    }
};


/*
Runtime: 26 ms, faster than 55.22% of C++ online submissions for Missing Number.
Memory Usage: 18 MB, less than 20.98% of C++ online submissions for Missing Number.
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0, i = 0;
        for (i = 0; i < nums.size(); ++i) {
            ans ^= (nums[i] ^ i);
        }
        return ans ^ i;
    }
};
