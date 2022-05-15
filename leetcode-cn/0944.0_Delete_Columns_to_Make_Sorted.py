'''
执行用时：68 ms, 在所有 Python3 提交中击败了93.84% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了56.16% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                ans += 1
        return ans 

'''
执行用时：128 ms, 在所有 Python3 提交中击败了67.02% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了21.75% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            n = len(col)
            for i in range(1, n):
                if col[i] < col[i - 1]:
                    ans += 1
                    break
        return ans 

'''
执行用时：68 ms, 在所有 Python3 提交中击败了94.45% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了41.77% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(1 if list(s) != sorted(s) else 0 for s in zip(*strs))
        