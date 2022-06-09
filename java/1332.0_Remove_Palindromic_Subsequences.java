/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Palindromic Subsequences.
Memory Usage: 41.9 MB, less than 43.06% of Java online submissions for Remove Palindromic Subsequences.
*/
class Solution {
    public int removePalindromeSub(String s) {
        return s.isEmpty() ? 0 : (s.equals(new StringBuilder(s).reverse().toString()) ? 1 : 2);
    }
}
