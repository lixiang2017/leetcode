/*
63 / 63 个通过测试用例
状态：通过
执行用时: 396 ms
内存消耗: 137 MB
提交时间：18 小时前

a - x - y - b
*/
class Solution {
public:
    typedef pair<int, int> pii;
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        int n = scores.size();
        vector<vector<pii>> g(n);
        for (auto &e: edges) {
            int x = e[0], y = e[1];
            g[x].emplace_back(-scores[y], y);
            g[y].emplace_back(-scores[x], x);
        }
        for (auto &vs: g) {
            if (vs.size() > 3) {
                nth_element(vs.begin(), vs.begin() + 2, vs.end());
                vs.resize(3);
            }
        }
        
        int ans = -1;
        for (auto &e: edges) {
            int x = e[0], y = e[1];
            for (auto &[score_a, a]: g[x])
                for (auto &[score_b, b]: g[y])
                    if (a != y && b != x && a != b)
                        ans = max(ans, -score_a + scores[x] + scores[y] - score_b);
        }
        return ans;
    }
};

