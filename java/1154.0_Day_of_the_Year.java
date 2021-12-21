/*
执行用时：33 ms, 在所有 Java 提交中击败了10.95% 的用户
内存消耗：40.2 MB, 在所有 Java 提交中击败了8.94% 的用户
通过测试用例：10957 / 10957
*/
class Solution {
    public int dayOfYear(String date) {
        return java.time.LocalDate.parse(date).getDayOfYear();
    }
}
