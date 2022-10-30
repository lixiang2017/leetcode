/*
执行用时：56 ms, 在所有 C# 提交中击败了98.68% 的用户
内存消耗：46.9 MB, 在所有 C# 提交中击败了40.77% 的用户
通过测试用例：3999 / 3999
*/
public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> symbolValues = new Dictionary<char, int> {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int ans = 0, n = s.Length;
        for (int i = 0; i < s.Length; ++i) {
            int value = symbolValues[s[i]];
            if (i < n - 1 && value < symbolValues[s[i + 1]]) {
                ans -= value;
            } else {
                ans += value;
            }
        }
        return ans;
    }
}
