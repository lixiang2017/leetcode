/*
DP

执行用时：1 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：50.7 MB, 在所有 Java 提交中击败了37.86% 的用户
通过测试用例：209 / 209
*/
class Solution {
    public int maxSubArray(int[] nums) {
        int ans = nums[0], pre = 0;
        for (int num: nums) {
            pre += num;
            ans = Math.max(ans, pre);
            if (pre < 0)
                pre = 0;
        }
        return ans;
    }
}


/*
segment tree

执行用时：8 ms, 在所有 Java 提交中击败了5.24% 的用户
内存消耗：52 MB, 在所有 Java 提交中击败了5.06% 的用户
通过测试用例：209 / 209
*/
class Solution {
    public class Status {
        public int lSum, rSum, mSum, iSum;

        public Status(int lSum, int rSum, int mSum, int iSum) {
            this.lSum = lSum;
            this.rSum = rSum;
            this.mSum = mSum;
            this.iSum = iSum;
        }
    }
    public int maxSubArray(int[] nums) {
        return getInfo(nums, 0, nums.length - 1).mSum;
    }

    public Status getInfo(int[] a, int l, int r) {
        if (l == r) {
            return new Status(a[l], a[l], a[l], a[l]);
        }
        int m = (l + r) >> 1;
        Status lSub = getInfo(a, l, m);
        Status rSub = getInfo(a, m + 1, r);
        return pushUp(lSub, rSub);
    }

    public Status pushUp(Status l, Status r) {
        int iSum = l.iSum + r.iSum;
        int lSum = Math.max(l.lSum, l.iSum + r.lSum);
        int rSum = Math.max(r.rSum, r.iSum + l.rSum);
        int mSum = Math.max(Math.max(l.mSum, r.mSum), l.rSum + r.lSum);
        return new Status(lSum, rSum, mSum, iSum);
    }
}

