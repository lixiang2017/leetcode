/*
binary search
T: O(logN)
S: O(1)
执行用时：4 ms, 在所有 C++ 提交中击败了70.10% 的用户
内存消耗：10.7 MB, 在所有 C++ 提交中击败了72.02% 的用户
通过测试用例：195 / 195
*/
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        while (i <= j) {
            int mid = (j - i) / 2 + i;
            if (nums[i] == target) return i;
            if (nums[mid] == target) return mid;
            if (nums[j] == target) return j;
            if (nums[i] < nums[mid]) {
                // 前半段更长，而且有序增大
                if (nums[i] < target && target < nums[mid]) {
                    j = mid - 1;
                } else {
                    i = mid + 1;
                }
            } else {
                // 后半段更长，而且有序增大
                if (nums[mid] < target && target < nums[j]) {
                    i = mid + 1;
                } else {
                    j = mid - 1;
                }
            }
        }
        return -1;
    }
};
