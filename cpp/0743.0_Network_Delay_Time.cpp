/*
不使用优先队列，适用于稠密图：

    不使用优先队列，但引入visited向量记录是否使用过了（使用过的意思是被当做中间节点 ）
    使用邻接矩阵表示邻接关系

执行用时：108 ms, 在所有 C++ 提交中击败了46.33% 的用户
内存消耗：40.3 MB, 在所有 C++ 提交中击败了18.80% 的用户
通过测试用例：52 / 52
*/

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<long long>> graph(n, vector<long long>(n, INT_MAX));
        for (int i = 0; i < n; ++i) {
            graph[i][i] = 0;
        }
        for (auto t: times) {
            graph[t[0] - 1][t[1] - 1] = t[2];
        }
        vector<bool> visited(n, false);

        for (int i = 0; i < n; i++) {
            // to find nearest unused node
            int min_id = -1;
            for (int j = 0; j < n; j++) {
                if (visited[j] == false && (min_id == -1 || graph[k - 1][j] < graph[k - 1][min_id])) {
                    min_id = j;
                }
            }
            visited[min_id] = true;
            // update dist
            for (int j = 0; j < n; ++j) {
                if (graph[k - 1][min_id] + graph[min_id][j] < graph[k - 1][j]) {
                    graph[k - 1][j] = graph[k - 1][min_id] + graph[min_id][j];
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (graph[k - 1][i] == INT_MAX) {
                return -1;
            }
            ans = max(ans, (int)graph[k - 1][i]);
        }
        return ans;
    }
};
