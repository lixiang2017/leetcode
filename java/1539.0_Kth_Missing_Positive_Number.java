/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：40.9 MB, 在所有 Java 提交中击败了65.45% 的用户
通过测试用例：84 / 84
*/
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            if (arr[i] - i - 1 >= k) {
                return k + i;
            }
        }
        return k + n;
    }
}
