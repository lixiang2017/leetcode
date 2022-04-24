/*
执行用时：1 ms, 在所有 Java 提交中击败了33.33% 的用户
内存消耗：38.3 MB, 在所有 Java 提交中击败了61.15% 的用户
通过测试用例：261 / 261
*/
class Solution {
    private static final HashMap<Integer, Integer> IDX_MAP = new HashMap<>();
    static {
        for (int i = 0; i <= 30; i++) {
            IDX_MAP.put(1 << i, i);
        }
    }

    public static final int lowbit(int x) {
        return x & (-x);
    }

    public int binaryGap(int n) {
        int last = 30, ans = 0;
        while (n != 0) {
            int lb = lowbit(n);
            int i = IDX_MAP.get(lb);
            ans = Math.max(ans, i - last);
            last = i;
            n -= lb;
        }
        return ans;
    }
}
