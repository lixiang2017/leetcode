class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        int n = min({s1.length(), s2.length(), s3.length()});
        int i = 0;
        while (i < n && s2[i] == s1[i] && s3[i] == s1[i]) {
            i++;
        }
        return i == 0 ? -1 : s1.length() + s2.length() + s3.length() - i * 3;
    }
};