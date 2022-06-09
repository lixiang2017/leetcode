/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Remove Palindromic Subsequences.
Memory Usage: 6.3 MB, less than 26.79% of C++ online submissions for Remove Palindromic Subsequences.
*/
class Solution {
public:
    int removePalindromeSub(string s) {
        return 2 - (s == string(s.rbegin(), s.rend())) - s.empty();
    }
};


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Remove Palindromic Subsequences.
Memory Usage: 6.1 MB, less than 78.83% of C++ online submissions for Remove Palindromic Subsequences.
*/
class Solution {
public:
    int removePalindromeSub(string s) {
        return 2 - equal(s.begin(), s.end(), s.rbegin()) - s.empty();
    }
};

