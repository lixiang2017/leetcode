/*
执行用时：348 ms, 在所有 C# 提交中击败了0.00% 的用户
内存消耗：65 MB, 在所有 C# 提交中击败了75.00% 的用户
通过测试用例：89 / 89
*/
public class Solution {
    public int MaxEqualRowsAfterFlips(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;
        IDictionary<string, int> dictionary = new Dictionary<string, int>();
        for (int i = 0; i < m; i++) {
            char[] arr = new char[n];
            Array.Fill(arr, '0');
            for (int j = 0; j < n; j++) {
                arr[j] = (char)('0' + (matrix[i][j] ^ matrix[i][0]));
            }
            string s = new string(arr);
            dictionary.TryAdd(s, 0);
            dictionary[s]++;
        }
        int ans = 0;
        foreach (KeyValuePair<string, int> pair in dictionary) {
            ans = Math.Max(ans, pair.Value);
        }
        return ans;
    }
}
