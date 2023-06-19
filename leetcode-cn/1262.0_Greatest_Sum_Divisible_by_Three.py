'''
执行用时：80 ms, 在所有 Python3 提交中击败了70.33% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了45.12% 的用户
通过测试用例：42 / 42
'''
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for cntb in [lb - 2, lb - 1, lb]:
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        ans = max(ans, sum(b[: cntb]) + sum(c[: cntc]))
        return ans + sum(a)

