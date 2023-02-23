/*
Runtime: 211 ms, faster than 93.30% of C++ online submissions for IPO.
Memory Usage: 82.1 MB, less than 23.74% of C++ online submissions for IPO.
*/
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects;
        for (int i = 0; i < n; i++) {
            projects.emplace_back(capital[i], profits[i]);
        }
        sort(projects.begin(), projects.end());
        priority_queue<int> q;
        int ptr = 0;
        for (int i = 0; i < k; i++) {
            while (ptr < n && projects[ptr].first <= w) {
                q.push(projects[ptr++].second);
            }
            if (q.empty()) {
                break;
            }
            w += q.top();
            q.pop();
        }
        return w;
    }
};
