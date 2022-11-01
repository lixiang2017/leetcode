/*
执行用时：160 ms, 在所有 C# 提交中击败了26.19% 的用户
内存消耗：64.3 MB, 在所有 C# 提交中击败了73.81% 的用户
通过测试用例：63 / 63
*/
public class Solution {
    public IList<string> LetterCasePermutation(string s) {
        IList<string> ans = new List<string>();
        Queue<StringBuilder> q = new Queue<StringBuilder>();
        q.Enqueue(new StringBuilder());
        while (q.Count > 0) {
            StringBuilder curr = q.Peek();
            if (curr.Length == s.Length) {
                ans.Add(curr.ToString());
                q.Dequeue();
            } else {
                int pos = curr.Length;
                if (char.IsLetter(s[pos])) {
                    StringBuilder next = new StringBuilder(curr.ToString());
                    next.Append((char) (s[pos] ^ 32));
                    q.Enqueue(next);
                }
                curr.Append(s[pos]);
            }
        }
        return ans;
    }
}
