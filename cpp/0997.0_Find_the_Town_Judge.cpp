/*
Runtime: 372 ms, faster than 5.03% of C++ online submissions for Find the Town Judge.
Memory Usage: 60.7 MB, less than 78.42% of C++ online submissions for Find the Town Judge.
*/
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> degree(n + 1, 0);
        for (auto &t: trust) {
            degree[t[0]]--;
            degree[t[1]]++;
        }
        for (int i = 1; i <= n; ++i) {
            if(degree[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
};
