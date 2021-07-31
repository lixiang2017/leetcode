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
        