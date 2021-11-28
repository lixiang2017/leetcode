'''
Hash Table

执行用时：68 ms, 在所有 Python3 提交中击败了94.03% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了89.97% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl, pl = len(s), len(p)
        if sl < pl:
            return []
        pcnt = [0] * 26
        for ch in p:
            pcnt[ord(ch) - ord('a')] += 1
        ans = []
        scnt = [0] * 26
        for i in range(pl):
            scnt[ord(s[i]) - ord('a')] += 1
        if scnt == pcnt:
            ans.append(0)
        for i in range(pl, len(s)):
            scnt[ord(s[i - pl]) - ord('a')] -= 1
            scnt[ord(s[i]) - ord('a')] += 1
            if scnt == pcnt:
                ans.append(i - pl + 1)

        return ans
