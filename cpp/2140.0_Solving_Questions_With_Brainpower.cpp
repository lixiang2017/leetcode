class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        long f[n + 1];
        memset(f, 0, sizeof(f));
        for (int i = 0; i < n; ++i) {
            f[i + 1] = max(f[i + 1], f[i]);
            auto &q = questions[i];
            int j = min(i + q[1] + 1, n);
            f[j] = max(f[j], f[i] + q[0]);
        }    
        return f[n];
    }
};