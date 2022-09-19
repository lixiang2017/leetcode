'''
longest,T:O(N),S:O(26)
Hash Table, to remember the earliest index

执行用时：32 ms, 在所有 Python3 提交中击败了90.28% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.99% 的用户
'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in seen:
                ans = max(ans, i - seen[ch] - 1)
            else:
                seen[ch] = i
        
        return ans


'''
执行用时：40 ms, 在所有 Python3 提交中击败了63.16% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.63% 的用户
'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max([s.rfind(c) - s.find(c) - 1 for c in s])


'''
执行用时：40 ms, 在所有 Python3 提交中击败了58.51% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.28% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if len(pos[idx]) <= 1:
                pos[idx].append(i)
            elif len(pos[idx]) == 2:
                pos[idx][-1] = i 
        
        for p in pos:
            if len(p) == 2:
                ans = max(ans, p[1] - p[0] - 1)
        return ans 
