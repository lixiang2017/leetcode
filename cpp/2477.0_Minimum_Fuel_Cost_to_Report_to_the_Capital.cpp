/*
DFS

Runtime: 1633 ms, faster than 16.67% of C++ online submissions for Minimum Fuel Cost to Report to the Capital.
Memory Usage: 225.7 MB, less than 16.67% of C++ online submissions for Minimum Fuel Cost to Report to the Capital.
*/
class Solution {
public:
    long long dfs(int x, int fa) {
        long long size = 1;
        for (auto& y : tree[x]) {
            if (y == fa) continue;
            size += dfs(y, x);
        }
        if (x != 0)
            ans += (size + seat - 1) / seat;
        return size;
    }

    long long ans = 0;
    int seat;
    unordered_map<int, vector<int>> tree;
    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        seat = seats;
        for (const auto& road : roads) {
            int a = road[0], b = road[1];
            tree[a].push_back(b);
            tree[b].push_back(a);
        }

        dfs(0, -1);
        return ans;
    }
};
