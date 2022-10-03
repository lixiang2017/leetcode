/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：39.8 MB, 在所有 Java 提交中击败了13.98% 的用户
通过测试用例：191 / 191
*/
class Solution {
    public boolean checkOnesSegment(String s) {
        return !s.contains("01");
    }
}
