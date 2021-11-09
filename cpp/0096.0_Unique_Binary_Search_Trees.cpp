/*
DP

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Unique Binary Search Trees.
Memory Usage: 6 MB, less than 64.16% of C++ online submissions for Unique Binary Search Trees.
*/
class Solution {
public:
    int numTrees(int n) {
        vector<int> memo(n + 1, 1);
        int nodes = 2;
        while (nodes <= n) {
            int count = 0;
            for (int i = 1; i <= nodes; i++) {
                int leftNodes = i - 1;
                int rightNodes = nodes - i;
                count += memo[leftNodes] * memo[rightNodes];
            }
            memo[nodes] = count;
            nodes++;
        }
        return memo[n];
    }
};
