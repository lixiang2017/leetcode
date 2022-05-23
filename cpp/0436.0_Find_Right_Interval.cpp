/*
执行用时：60 ms, 在所有 C++ 提交中击败了78.39% 的用户
内存消耗：24.4 MB, 在所有 C++ 提交中击败了84.09% 的用户
通过测试用例：19 / 19
*/
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<pair<int, int>> starts;
        for (int i = 0; i < n; i++) {
            starts.emplace_back(intervals[i][0], i);
        }
        sort(starts.begin(), starts.end());
        auto comp = [](const pair<int, int>& p, int b) {
            return p.first < b;
        };

        vector<int> ans(n, -1);
        for (int i = 0; i < n; i++) { 
            int end = intervals[i][1];
            if (starts.back().first < end) continue;
            auto it = lower_bound(starts.begin(), starts.end(), end, comp);
            ans[i] = it->second;
        }
        return ans;
    }
};

