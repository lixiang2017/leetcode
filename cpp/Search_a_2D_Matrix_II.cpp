/*
approach: Greedy
compare from top-right to bottom-left
Time: O(M + N)
Space: O(1)

You are here!
Your runtime beats 43.18 % of cpp submissions.
You are here!
Your memory usage beats 65.96 % of cpp submissions.
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int M = matrix.size(), N = matrix[0].size();
        int i = 0, j = N - 1;
        while (i < M and j >= 0) {
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] > target) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
};