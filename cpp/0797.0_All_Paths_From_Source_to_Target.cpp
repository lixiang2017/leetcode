/*
Backtracking

Runtime: 20 ms, faster than 51.98% of C++ online submissions for All Paths From Source to Target.
Memory Usage: 15.6 MB, less than 31.58% of C++ online submissions for All Paths From Source to Target.
*/
class Solution {
public:
    vector<vector<int>> paths;
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();       
        vector<int> p(1, 0);
        backtracking(n, graph, 0, p);
        return paths;
    }
    
    void backtracking(int n, vector<vector<int>>& graph, int node, vector<int> p) {
        if (node == n - 1) {
            paths.push_back(p);
            return;
        }
        for (auto child: graph[node]) {
            p.push_back(child);
            backtracking(n, graph, child, p);
            p.pop_back();
        }
    }
};

/*
to use vector<int>& p, instead of vector<int> p

Runtime: 12 ms, faster than 83.33% of C++ online submissions for All Paths From Source to Target.
Memory Usage: 11.9 MB, less than 63.83% of C++ online submissions for All Paths From Source to Target.
*/
class Solution {
public:
    vector<vector<int>> paths;
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();       
        vector<int> p(1, 0);
        backtracking(n, graph, 0, p);
        return paths;
    }
    
    void backtracking(int n, vector<vector<int>>& graph, int node, vector<int>& p) {
        if (node == n - 1) {
            paths.push_back(p);
            return;
        }
        for (auto child: graph[node]) {
            p.push_back(child);
            backtracking(n, graph, child, p);
            p.pop_back();
        }
    }
};



/*
Runtime: 12 ms, faster than 83.33% of C++ online submissions for All Paths From Source to Target.
Memory Usage: 10.6 MB, less than 85.55% of C++ online submissions for All Paths From Source to Target.
*/
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> paths;
        vector<int> p(1, 0);
        backtracking(n, graph, paths, 0, p);
        return paths;
    }
    
    void backtracking(int n, vector<vector<int>>& graph, vector<vector<int>>& paths, int node, vector<int>& p) {
        if (node == n - 1) {
            paths.push_back(p);
            return;
        }
        for (auto child: graph[node]) {
            p.push_back(child);
            backtracking(n, graph, paths, child, p);
            p.pop_back();
        }
    }
};


