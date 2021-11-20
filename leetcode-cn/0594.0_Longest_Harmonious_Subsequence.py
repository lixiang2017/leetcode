'''
Hash Table + Sort

执行用时：260 ms, 在所有 Python3 提交中击败了90.70% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了30.73% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        ks = sorted(c.keys())
        ans = 0
        for i in range(len(ks) - 1):
            if ks[i + 1] - ks[i] == 1:
                ans = max(ans, c[ks[i]] + c[ks[i + 1]])
        return ans
