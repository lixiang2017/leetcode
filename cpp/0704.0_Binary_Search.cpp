/*
执行用时：32 ms, 在所有 C++ 提交中击败了72.96% 的用户
内存消耗：26.9 MB, 在所有 C++ 提交中击败了47.86% 的用户
通过测试用例：46 / 46

[-1]
2
*/
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // 当时的这个代码还能通过。但是现在已经不行了。原因就是这个代码错了，应该是 size() - 1
        // int l = 0, r = nums.size() - 1; 
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


/*
Runtime: 39 ms, faster than 80.20% of C++ online submissions for Binary Search.
Memory Usage: 27.5 MB, less than 92.40% of C++ online submissions for Binary Search.
*/
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int pivot, left = 0, right = nums.size() - 1;
        while (left <= right) {
            pivot = left + (right - left) / 2;
            if (nums[pivot] == target) return pivot;
            if (target < nums[pivot]) right = pivot - 1;
            else left = pivot + 1;
        }
        return -1;
    }
};