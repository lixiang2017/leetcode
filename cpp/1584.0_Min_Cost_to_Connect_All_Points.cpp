/*
prim

执行用时：88 ms, 在所有 C++ 提交中击败了91.38% 的用户
内存消耗：26.2 MB, 在所有 C++ 提交中击败了77.34% 的用户
通过测试用例：72 / 72
*/
class Solution {
public:
    int prim(vector<vector<int>>& points, int start) {
        int n = points.size();
        int cost = 0;
        // graph
        vector<vector<int>> g(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                g[i][j] = dist;
                g[j][i] = dist;
            }
        }
        // low_cost, for every not-added nodes to MST
        vector<int> low_cost(n, INT_MAX);
        // whether added to MST. -1, not added; 0, added.
        vector<int> added(n, -1);
        
        // start
        added[start] = 0;
        for (int i = 0; i < n; i++) {
            if (i == start) continue;
            low_cost[i] = g[i][start];
        }
        // left n-1 nodes, need to add to MST
        for (int k = 1; k < n; k++) {
            // find closest node to MST 
            int min_idx = -1, min_cost = INT_MAX;
            for (int j = 0; j < n; j++) {
                if (added[j] == 0) continue;
                if (low_cost[j] < min_cost) {
                    min_idx = j;
                    min_cost = low_cost[j];
                }
            }
            // add node min_idx to MST 
            cost += min_cost;
            added[min_idx] = 0;
            low_cost[min_idx] = -1;
            // update low_cost
            for (int j = 0; j < n; j++) {
                if (added[j] == -1 && g[j][min_idx] < low_cost[j]) {
                    low_cost[j] = g[j][min_idx];
                }
            }
        }
        return cost;
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        return prim(points, 0);
    }
};



/*
prim + pq(min-heap)

执行用时：144 ms, 在所有 C++ 提交中击败了79.51% 的用户
内存消耗：59 MB, 在所有 C++ 提交中击败了36.65% 的用户
通过测试用例：72 / 72
*/
class Solution {
public:
    int prim(vector<vector<int>>& points, int start) {
        int n = points.size();
        int cost = 0;
        // graph
        vector<vector<int>> g(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                g[i].push_back(j);
                g[j].push_back(i);
            }
        }
        // low_cost, for every not-added nodes to MST
        vector<int> low_cost(n, INT_MAX);
        // whether added to MST. -1, not added; 0, added.
        vector<int> added(n, -1);
        // added count
        int add_cnt = 0;
        // (distance, node_idx), distance to MST 
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<> > pq;

        // start from `start` node
        pq.push(make_pair(0, start));
        while (!pq.empty()) {
            auto [dist, i] = pq.top();
            pq.pop();
            if (added[i] == 0) continue;
            added[i] = 0;
            cost += dist;
            if (++add_cnt == n) {
                return cost;
            }
            // update low_cost, pq
            for (auto j: g[i]) {
                int weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                if (added[j] == -1 && low_cost[j] > weight) {
                    low_cost[j] = weight;
                    pq.push(make_pair(weight, j));
                }
            }
        }
        return cost;
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        return prim(points, 0);
    }
};


/*
kruskal, _union

执行用时：452 ms, 在所有 C++ 提交中击败了59.92% 的用户
内存消耗：56.9 MB, 在所有 C++ 提交中击败了48.10% 的用户
通过测试用例：72 / 72
*/
class UnionFind {
public:
    vector<int> p;     // parent
    vector<int> rank;  // rank, depth
    vector<int> size;  // count for each part
    vector<int> len;   // cost, total distance for each part
    int num;           // the number of nodes 
    int set_count;     // number of parts
    UnionFind(int n): p(n), rank(n), len(n, 0), size(n, 1), num(n), set_count(n) {
        for (int i = 0; i < n; i++) {
            p[i] = i;
        }
    }

    int find(int x) {
        if (x == p[x]) {
            return x;
        }
        p[x] = find(p[x]);
        return p[x];
    }

    int _union(int x, int y, int length){
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            // make sure rootx >= rooty, so rooty -> rootx
            if (rank[rootx] < rank[rooty])
                swap(rootx, rooty);
            p[rooty] = rootx;
            if (rank[rootx] == rank[rooty]) {
                rank[rootx]++;
            }
            size[rootx] += size[rooty];
            len[rootx] += len[rooty] + length;
            set_count--;
            // return total_cost of MST 
            if (size[rootx] == num) {
                return len[rootx];
            }
        }
        return -1;
    }
};

struct Edge {
    int start;  // node1
    int end;    // node2
    int len;    // len, cost, dist
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int cost = 0;
        int n = points.size();
        UnionFind uf(n);
        vector<Edge> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]); 
                Edge edge = {i, j, len};
                edges.emplace_back(edge);
            }
        }
        // sort
        sort(edges.begin(), edges.end(), [&](const auto&a, const auto& b) {
            return a.len < b.len;
        });

        // union
        for (auto e: edges) {
            cost = uf._union(e.start, e.end, e.len);
            if (cost != -1) return cost;
        }
        return 0;
    }
};



/*
执行用时：436 ms, 在所有 C++ 提交中击败了64.16% 的用户
内存消耗：56.8 MB, 在所有 C++ 提交中击败了61.71% 的用户
通过测试用例：72 / 72
*/
class DisjointSetUnion {
private:
    vector<int> f, size;   // father, size
    int n;

public:
    DisjointSetUnion(int _n) {
        n = _n;
        size.resize(n, 1);
        f.resize(n);
        for (int i = 0; i < n; i++) {
            f[i] = i;
        }
    }

    int find(int x) {
        return f[x] == x ? x : f[x] = find(f[x]); 
    }

    int unionSet(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) {
            return false;
        }
        // make suer size_fx >= size_fy, so fy -> fx
        if (size[fx] < size[fy]) {
            swap(fx, fy);
        }
        f[fy] = fx;
        size[fx] += f[fy];
        return true;
    }
};

struct Edge {
    int len, x, y;
    Edge(int len, int x, int y): len(len), x(x), y(y) {};
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        auto dist = [&](int i, int j) -> int {
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]); 
        };
        int cost = 0, num = 1;
        int n = points.size();
        DisjointSetUnion dsu(n);
        vector<Edge> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                edges.emplace_back(dist(i, j), i, j);
            }
        }
        // sort
        sort(edges.begin(), edges.end(), [&](const auto&a, const auto& b) {
            return a.len < b.len;
        });

        // union
        for (auto& [len, x, y]: edges) {
            if (dsu.unionSet(x, y)) {
                cost += len;
                num++;
                if (num == n)
                    return cost;
            }
        }
        return cost;
    }
};


