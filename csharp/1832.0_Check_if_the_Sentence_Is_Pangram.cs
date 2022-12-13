/*
执行用时：80 ms, 在所有 C# 提交中击败了14.81% 的用户
内存消耗：37.2 MB, 在所有 C# 提交中击败了11.11% 的用户
通过测试用例：79 / 79
*/
public class Solution {
    public bool CheckIfPangram(string sentence) {
        return (new HashSet<char>(sentence)).Count == 26;
    }
}
