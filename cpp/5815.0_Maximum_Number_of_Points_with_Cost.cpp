/*
DP
执行用时：216 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：80.1 MB, 在所有 C++ 提交中击败了100.00% 的用户
*/
typedef signed long long ll;

#define FOR(x, to) for(x = 0; x < (to); x++)
#define ZERO(a) memset(a, 0, sizeof(a))

ll from[101010];

class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int H = points.size();
        int W = points[0].size();
        ZERO(from);
        int y, x;
        FOR(y, H) {
            FOR(x, W) from[x] += points[y][x];
            FOR(x, W - 1) from[x + 1] = max(from[x + 1], from[x] - 1);
            for(x = W - 1; x > 0; x--) from[x - 1] = max(from[x - 1], from[x] - 1);
        }

        return *max_element(from, from + W);
    }
};
