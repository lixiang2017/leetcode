'''
二进制枚举

执行用时：2328 ms, 在所有 Python3 提交中击败了16.28% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了93.80% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxx = reduce(operator.or_, nums)
        n = len(nums)
        ans = 0
        for state in range(1 << n):
            v = 0
            for i in range(n):
                if (1 << i) & state:
                    v |= nums[i]
            if v == maxx:
                ans += 1
        return ans 
