/*
中心扩散法
T： O（N^2)
S: O(1)

Runtime: 6 ms, faster than 60.83% of Java online submissions for Palindromic Substrings.
Memory Usage: 42 MB, less than 65.16% of Java online submissions for Palindromic Substrings.
*/
class Solution {
    int num = 0;
    public int countSubstrings(String s) {
        for (int i = 0; i < s.length(); ++i) {
            count(s, i, i);
            count(s, i, i + 1);
        }
        return num;
    }
    
    public void count(String s, int start, int end) {
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            num++;
            start--;
            end++;
        }
    }
}
