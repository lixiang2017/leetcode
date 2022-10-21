'''
hash table

执行用时：84 ms, 在所有 Python3 提交中击败了81.87% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了29.67% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i 
        return -1
