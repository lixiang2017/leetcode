/*
执行用时：32 ms, 在所有 Java 提交中击败了91.00% 的用户
内存消耗：39.7 MB, 在所有 Java 提交中击败了98.65% 的用户
通过测试用例：206 / 206
*/

class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> set = new HashSet<>();
        for (int c: candyType) {
            set.add(c);
        }
        return Math.min(set.size(), candyType.length >> 1);
    }
}
