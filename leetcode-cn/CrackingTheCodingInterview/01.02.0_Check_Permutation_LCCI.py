'''
sort 

执行用时：36 ms, 在所有 Python3 提交中击败了62.84% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.52% 的用户
通过测试用例：23 / 23
'''
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

'''
执行用时：28 ms, 在所有 Python3 提交中击败了97.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了29.73% 的用户
通过测试用例：23 / 23
'''
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

'''
执行用时：36 ms, 在所有 Python3 提交中击败了62.84% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了99.48% 的用户
通过测试用例：23 / 23
'''
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        c1, c2 = [0] * 26, [0] * 26
        for ch in s1:
            c1[ord(ch) - ord('a')] += 1
        for ch in s2:
            c2[ord(ch) - ord('a')] += 1
        return c1 == c2 
        