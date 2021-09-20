/*

执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：36.3 MB, 在所有 Java 提交中击败了93.25% 的用户
通过测试用例：58 / 58
*/
class Solution {
    public int lengthOfLastWord(String s) {
        int r = s.length() - 1;
        while (r >= 0 && s.charAt(r) == ' ') {
            r--;
        }
        int wordLength = 0;
        while (r >= 0 && s.charAt(r) != ' ') {
            r--;
            wordLength++;
        }
        return wordLength;
    }
}
