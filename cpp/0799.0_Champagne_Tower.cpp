/*
执行用时：16 ms, 在所有 C++ 提交中击败了34.50% 的用户
内存消耗：13.6 MB, 在所有 C++ 提交中击败了59.10% 的用户
通过测试用例：312 / 312
*/
class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<double> row = {(double)poured};
        for (int i = 1; i <= query_row; ++i) {
            vector<double> nextRow(i + 1, 0.0);
            for (int j = 0; j < row.size(); ++j) {
                double volume = row[j];
                if (volume > 1) {
                    nextRow[j] += (row[j] - 1) / 2;
                    nextRow[j + 1] += (row[j] - 1) / 2;
                }
            }
            row = nextRow;
        }
        return min(1.0, row[query_glass]);
    }
};
