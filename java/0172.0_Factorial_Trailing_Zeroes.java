/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：38 MB, 在所有 Java 提交中击败了68.32% 的用户
通过测试用例：500 / 500
*/
class Solution {
    public int trailingZeroes(int n) {
        return n < 5 ? 0: n / 5 + trailingZeroes(n / 5);
    }
}
