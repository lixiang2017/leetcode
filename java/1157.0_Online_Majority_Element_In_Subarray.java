/*
brute force

执行用时：1245 ms, 在所有 Java 提交中击败了10.45% 的用户
内存消耗：51 MB, 在所有 Java 提交中击败了97.01% 的用户
通过测试用例：32 / 32
*/
class MajorityChecker {
    private int[] arr;

    public MajorityChecker(int[] arr) {
        this.arr = arr;
    }
    
    public int query(int left, int right, int threshold) {
        int[] map = new int[20001];
        for (int i = left; i <= right; i++) {
            if (++map[arr[i]] >= threshold) {
                return arr[i];
            }
        }
        return -1;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.query(left,right,threshold);
 */
