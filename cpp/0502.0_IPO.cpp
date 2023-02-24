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


/*
执行用时：204 ms, 在所有 C++ 提交中击败了27.94% 的用户
内存消耗：74.8 MB, 在所有 C++ 提交中击败了91.50% 的用户
通过测试用例：35 / 35
*/
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<int> index(n);
        for (int i = 0; i < n; i++) index[i] = i;
        sort(index.begin(), index.end(), [&](int i, int j){
            return capital[i] < capital[j];
        });
        priority_queue<int> q;
        int i = 0;
        while (k-- > 0) {
            while (i < n && capital[index[i]] <= w) q.emplace(profits[index[i++]]);
            if (q.empty()) break;
            w += q.top();
            q.pop();
        }
        return w;
    }
};

