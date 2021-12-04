'''
执行用时：48 ms, 在所有 Python3 提交中击败了84.58% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.33% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        return all(c <= mc[k] for k, c in rc.items())
        