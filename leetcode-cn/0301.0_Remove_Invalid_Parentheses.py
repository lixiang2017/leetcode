'''
DFS
T: O(2^N)
S: O(N)

执行用时：2192 ms, 在所有 Python3 提交中击败了10.18% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了50.36% 的用户
通过测试用例：127 / 127
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for ch in s:
            if ch == '(':
                l += 1
            elif ch == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        N = len(s)
        L = N - l - r 
        ans = set()

        def dfs(i, left, right, subseq):
            if len(subseq) == L and left == 0 and right == 0:
                ans.add(subseq)
                return 
            if i >= N:
                return 
            if s[i] == '(':
                # choose
                dfs(i + 1, left + 1, right, subseq + s[i])
                # not choose
                dfs(i + 1, left, right, subseq)
            elif s[i] == ')':
                # choose
                if left > 0:
                    dfs(i + 1, left - 1, right, subseq + s[i])
                # not choose
                dfs(i + 1, left, right, subseq)
            else:
                # choose s[i]
                dfs(i + 1, left, right, subseq + s[i])

        dfs(0, 0, 0, '')
        return list(ans)
