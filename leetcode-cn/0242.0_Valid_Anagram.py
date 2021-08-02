'''
Hash Table,T:O(N),S:O(52)

执行用时：52 ms, 在所有 Python3 提交中击败了74.10% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了46.70% 的用户
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = [0] * 26, [0] * 26
        for ch in s:
            ss[ord(ch) - ord('a')] += 1
        for ch in t:
            tt[ord(ch) - ord('a')] += 1
        return ss == tt


'''
Sort,T:O(NlogN)
执行用时：60 ms, 在所有 Python3 提交中击败了51.43% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.01% 的用户
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
