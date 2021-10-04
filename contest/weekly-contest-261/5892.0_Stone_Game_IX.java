/*
执行用时：3 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：49.9 MB, 在所有 Java 提交中击败了100.00% 的用户
通过测试用例：93 / 93
*/
class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] mod = new int[3];
        for (int stone: stones) {
            mod[stone % 3]++;
        }
        if (mod[0] % 2 != 0) {
            return Math.abs(mod[1] - mod[2]) > 2;
        } else {
            return mod[1] > 0 && mod[2] > 0;
        }
    }
}
