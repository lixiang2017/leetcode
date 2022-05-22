/*
执行用时：56 ms, 在所有 C++ 提交中击败了68.03% 的用户
内存消耗：27.8 MB, 在所有 C++ 提交中击败了40.39% 的用户
通过测试用例：13 / 13
*/
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        srand((unsigned)time(NULL));
        randomized_quicksort(nums, 0, (int)nums.size() - 1);
        return nums;
    }

    void randomized_quicksort(vector<int>& nums, int l, int r) {
        if (l >= r) return;
        int pos = randomized_partition(nums, l, r);
        randomized_quicksort(nums, l, pos - 1);
        randomized_quicksort(nums, pos + 1, r);
    }

    int randomized_partition(vector<int>& nums, int l, int r) {
        int i = rand() % (r - l + 1) + l;
        swap(nums[r], nums[i]);
        int pivot = nums[r];
        i = l - 1;
        for (int j = l; j <= r - 1; ++j) {
            if (nums[j] <= pivot) {
                ++i;
                swap(nums[i], nums[j]);
            }
        }
        swap(nums[i + 1], nums[r]);
        return i + 1;
    }
};

