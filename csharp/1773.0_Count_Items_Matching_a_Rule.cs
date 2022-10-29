/*
执行用时：128 ms, 在所有 C# 提交中击败了60.87% 的用户
内存消耗：52.4 MB, 在所有 C# 提交中击败了91.30% 的用户
通过测试用例：92 / 92
*/
public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        int index = new Dictionary<string, int>() {
            {"type", 0}, {"color", 1}, {"name", 2}
        }[ruleKey];
        int ans = 0;
        foreach (IList<string> item in items) {
            if (item[index].Equals(ruleValue)) {
                ans++;
            }
        }
        return ans;
    }
}
