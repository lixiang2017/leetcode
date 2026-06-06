class SegmentTree {
    private final int[] max;

    public SegmentTree(int[] a) {
        int n = a.length;
        max = new int[2 << (32 - Integer.numberOfLeadingZeros(n - 1))];
        build(a, 1, 0, n - 1);
    }

    public int findFirstAndUpdate(int o, int l, int r, int x) {
        if (max[o] < x) {
            return -1;
        }
        if (l == r) {
            max[o] = -1;
            return l;
        }
        int m = (l + r) / 2;
        int i = findFirstAndUpdate(o * 2, l, m, x);
        if (i < 0) {
            i = findFirstAndUpdate(o * 2 + 1, m + 1, r, x);
        }
        maintain(o);
        return i;
    }

    private void maintain(int o) {
        max[o] = Math.max(max[o * 2], max[o * 2 + 1]);
    }

    private void build(int[] a, int o, int l, int r) {
        if (l == r) {
            max[o] = a[l];
            return;
        }
        int m = (l + r) / 2;
        build(a, o * 2, l, m);
        build(a, o * 2 + 1, m + 1, r);
        maintain(o);
    }
}

class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        SegmentTree t = new SegmentTree(baskets);
        int n = baskets.length;
        int ans = 0;
        for (int x: fruits) {
            if (t.findFirstAndUpdate(1, 0, n - 1, x) < 0) {
                ans++;
            }
        }
        return ans;
    }
}