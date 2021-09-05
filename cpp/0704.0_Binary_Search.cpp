/*
执行用时：32 ms, 在所有 C++ 提交中击败了72.96% 的用户
内存消耗：26.9 MB, 在所有 C++ 提交中击败了47.86% 的用户
通过测试用例：46 / 46
*/
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l <= r) {
            int mid = ((r - l) >> 1) + l;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
};
