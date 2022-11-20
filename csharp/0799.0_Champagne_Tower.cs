/*
执行用时：16 ms, 在所有 C# 提交中击败了100.00% 的用户
内存消耗：29.2 MB, 在所有 C# 提交中击败了90.91% 的用户
通过测试用例：312 / 312
*/
public class Solution {
    public double ChampagneTower(int poured, int query_row, int query_glass) {
        double[] row = {poured};
        for (int i = 1; i <= query_row; ++i) {
            double[] nextRow = new double[i + 1];
            for (int j = 0; j < i; j++) {
                if (row[j] > 1) {
                    nextRow[j] += (row[j] - 1) / 2;
                    nextRow[j + 1] += (row[j] - 1) / 2;
                }
            }
            row = nextRow;
        }
        return Math.Min(1, row[query_glass]);
    }
}
