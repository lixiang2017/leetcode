/*
执行用时：2 ms, 在所有 Java 提交中击败了13.68% 的用户
内存消耗：37 MB, 在所有 Java 提交中击败了6.79% 的用户
通过测试用例：550 / 550
*/

class Solution {
    public boolean detectCapitalUse(String word) {
        if (word.toLowerCase().equals(word)) return true;
        if (word.toUpperCase().equals(word)) return true;
        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) == word.toUpperCase().charAt(i)) {
                return false;
            }
        }
        return true;
    }
}


/*
执行用时：1 ms, 在所有 Java 提交中击败了98.19% 的用户
内存消耗：36.8 MB, 在所有 Java 提交中击败了46.92% 的用户
通过测试用例：550 / 550
*/
class Solution {
    public boolean detectCapitalUse(String word) {
        int diff = 0;
        for (char c: word.toCharArray()) {
            diff += Character.toLowerCase(c) - c;
        }
        // all upper || all lower || ...
        return diff/32 == word.length() || diff == 0 || diff==32 && word.charAt(0)>='A' && word.charAt(0) <= 'Z';
    }
}
