/*
Hash Set

执行用时：232 ms, 在所有 C# 提交中击败了92.00% 的用户
内存消耗：57.8 MB, 在所有 C# 提交中击败了44.00% 的用户
通过测试用例：206 / 206
*/
public class Solution {
    public int DistributeCandies(int[] candyType) {
        return Math.Min(candyType.ToHashSet().Count(), candyType.Count() / 2);
    }
}
