/*
DP

执行用时：64 ms, 在所有 C++ 提交中击败了99.80% 的用户
内存消耗：66 MB, 在所有 C++ 提交中击败了93.39% 的用户
通过测试用例：209 / 209
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0], pre = 0;
        for (auto x: nums) {
            pre += x;
            ans = max(ans, pre);
            if (pre < 0)
                pre = 0;
        }
        return ans;
    }
};


/*
segment tree

执行用时：84 ms, 在所有 C++ 提交中击败了82.80% 的用户
内存消耗：66.1 MB, 在所有 C++ 提交中击败了80.05% 的用户
通过测试用例：209 / 209
*/
class Solution {
public:
    // segment tree, information need to be maintained
    struct Status {
        // for a certain interval [l, r], inclusive l, r
        // from index_l, max sum
        int lSum;
        // ended with index_r, max_sum
        int rSum;
        // maximum subarry, for [l, r]
        int mSum;
        // all sum for range [l, r]
        int iSum;
    };

    Status pushUp(Status l, Status r) {
        int iSum = l.iSum + r.iSum;
        int lSum = max(l.lSum, l.iSum + r.lSum);
        int rSum = max(r.rSum, r.iSum + l.rSum);
        int mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum);
        return (Status) {lSum, rSum, mSum, iSum};
    }

    Status get(vector<int> &a, int l, int r) {
        if (l == r) {
            return (Status) {a[l], a[l], a[l], a[l]};
        }
        int m = (l + r) >> 1;
        Status lSub = get(a, l, m);
        Status rSub = get(a, m + 1, r);
        return pushUp(lSub, rSub);
    }

    int maxSubArray(vector<int>& nums) {
        return get(nums, 0, nums.size() - 1).mSum;
    }
};

