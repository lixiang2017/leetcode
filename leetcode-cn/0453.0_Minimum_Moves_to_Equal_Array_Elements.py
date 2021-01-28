'''
approach #1: n-1个元素+1等价于一个元素-1

approach #2:
/*
*建立方程等式,设至少需要移动x次
*那么最后达到平衡的那个数为(数组最小值+x)
*所以平衡后数组元素之和为N*(数组最小值+x)
*移动过程中增加了x*(N-1)
*得：初始数组各元素之和+x*(N-1)=N*(数组最小值+x)
*求出x即可
*/ 


Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：
280 ms, 在所有 Python 提交中击败了11.94%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了15.04%的用户
'''

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
        