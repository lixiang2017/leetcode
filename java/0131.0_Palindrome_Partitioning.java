/*
backtracking

Runtime: 8 ms, faster than 82.28% of Java online submissions for Palindrome Partitioning.
Memory Usage: 53.2 MB, less than 47.40% of Java online submissions for Palindrome Partitioning.
*/

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(0, result, new ArrayList<String>(), s);
        return result;
    }
    
    void dfs(int start, List<List<String>> result, List<String> currentList, String s) {
        if (start >= s.length()) {
            result.add(new ArrayList<String>(currentList));
        }
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                currentList.add(s.substring(start, end + 1));
                dfs(end + 1, result, currentList, s);
                currentList.remove(currentList.size() - 1);
            }
        }
    }
    
    boolean isPalindrome(String s, int low, int high) {
        while (low < high) {
            if (s.charAt(low++) != s.charAt(high--)) return false;
        }
        return true;
    }
}


/*
backtracking with DP

Runtime: 29 ms, faster than 8.50% of Java online submissions for Palindrome Partitioning.
Memory Usage: 150.8 MB, less than 20.02% of Java online submissions for Palindrome Partitioning.
*/
class Solution {
    public List<List<String>> partition(String s) {
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(0, result, new ArrayList<String>(), s, dp);
        return result;
    }
    
    void dfs(int start, List<List<String>> result, List<String> currentList, 
             String s, boolean[][] dp) {
        if (start >= s.length()) {
            result.add(new ArrayList<String>(currentList));
        }
        for (int end = start; end < s.length(); end++) {
            // if (isPalindrome(s, start, end)) 
            if (s.charAt(start) == s.charAt(end) && (end - start <= 2 || dp[start + 1][end - 1])){
                dp[start][end] = true;
                currentList.add(s.substring(start, end + 1));
                dfs(end + 1, result, currentList, s, dp);
                currentList.remove(currentList.size() - 1);
            }
        }
    }
    
}
