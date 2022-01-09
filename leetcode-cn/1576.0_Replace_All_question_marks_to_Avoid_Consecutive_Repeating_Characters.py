'''
T: O(N)
S: O(N)

执行用时：24 ms, 在所有 Python3 提交中击败了97.95% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.72% 的用户
通过测试用例：776 / 776
'''
class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        n = len(s)
        for i, ch in enumerate(s):
            if ch != '?':
                ans.append(ch)
                continue
            candidates = set(['a', 'b', 'c'])
            if i - 1 >= 0:
                # candidates.discard(s[i - 1]) # wrong
                candidates.discard(ans[i - 1])
            if i + 1 < n:
                candidates.discard(s[i + 1])
            ans.append(candidates.pop())
            
        return ''.join(ans)

'''
T: O(N)
S: O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了6.15%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.64%的用户
通过测试用例：
776 / 776
'''
class Solution:
    def modifyString(self, s: str) -> str:
        ss = list(s)
        n = len(ss)
        for i in range(n):
            if ss[i] == '?':
                for ch in 'abc':
                    if not (i > 0 and ss[i - 1] == ch or i < n - 1 and s[i + 1] == ch):
                        ss[i] = ch 
                        break
        return ''.join(ss)
