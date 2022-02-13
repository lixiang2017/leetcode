/*
执行用时：35 ms, 在所有 Java 提交中击败了10.90% 的用户
内存消耗：41.6 MB, 在所有 Java 提交中击败了5.04% 的用户
通过测试用例：353 / 353
*/

class Solution {
    public boolean isMatch(String s, String p) {
        return s.matches(p);
    }
}


/*
执行用时：32 ms, 在所有 Java 提交中击败了11.51% 的用户
内存消耗：41.5 MB, 在所有 Java 提交中击败了5.04% 的用户
通过测试用例：353 / 353
*/

import java.util.regex.Pattern;

class Solution {
    public boolean isMatch(String s, String p) {
        return Pattern.matches(p, s);
    }
}
