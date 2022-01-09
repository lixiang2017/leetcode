/*
backtracking

Runtime: 123 ms, faster than 55.24% of C++ online submissions for Palindrome Partitioning.
Memory Usage: 49.1 MB, less than 99.57% of C++ online submissions for Palindrome Partitioning.
*/

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> currentList;
        dfs(result, s, 0, currentList);
        return result;
    }
    
    void dfs(vector<vector<string>> &result, string &s, int start, vector<string> &currentList) {
        if (start >= s.length())
            result.push_back(currentList);
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                currentList.push_back(s.substr(start, end - start + 1));
                dfs(result, s, end + 1, currentList);
                currentList.pop_back();
            }
        }
    }
    
    bool isPalindrome(string &s, int low, int high) {
        while (low < high) {
            if (s[low++] != s[high--]) return false;
        }
        return true;
    }
};


/*
Runtime: 88 ms, faster than 88.82% of C++ online submissions for Palindrome Partitioning.
Memory Usage: 49.2 MB, less than 89.38% of C++ online submissions for Palindrome Partitioning.
*/
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int len = s.length();
        vector<vector<bool>> dp(len, vector<bool> (len, false));
        vector<vector<string>> result;
        vector<string> currentList;
        dfs(result, s, 0, currentList, dp);
        return result;
    }
    
    void dfs(vector<vector<string>> &result, string &s, int start, 
             vector<string> &currentList, vector<vector<bool>> &dp) {
        if (start >= s.length())
            result.push_back(currentList);
        for (int end = start; end < s.length(); end++) {
            if (s[start] == s[end] && (end - start <= 2 || dp[start + 1][end - 1])) {
                dp[start][end] = true;
                currentList.push_back(s.substr(start, end - start + 1));
                dfs(result, s, end + 1, currentList, dp);
                currentList.pop_back();
            }
        }
    }
    
};
