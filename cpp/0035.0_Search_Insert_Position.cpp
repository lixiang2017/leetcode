/*
执行用时：4 ms, 在所有 C++ 提交中击败了74.07% 的用户
内存消耗：9.5 MB, 在所有 C++ 提交中击败了8.42% 的用户
通过测试用例：64 / 64
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = ((r - l) >> 1) + l;
            if (nums[mid] >= target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return r + 1;
    }
};



/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：9.5 MB, 在所有 C++ 提交中击败了11.89% 的用户
通过测试用例：64 / 64
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }
};


/*
Runtime: 3 ms, faster than 90.12% of C++ online submissions for Search Insert Position.
Memory Usage: 9.7 MB, less than 31.02% of C++ online submissions for Search Insert Position.
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
                right = mid - 1; 
            } else {
                left = mid + 1;
            }
        }
        return left;        
    }
};


/*
Runtime: 6 ms, faster than 47.17% of C++ online submissions for Search Insert Position.
Memory Usage: 9.7 MB, less than 77.52% of C++ online submissions for Search Insert Position.
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
                right = mid - 1; 
            } else {
                left = mid + 1;
            }
        }
        return right + 1;        
    }
};
