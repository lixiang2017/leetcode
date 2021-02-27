'''
approach: Sort + Permutation

执行用时：16 ms, 在所有 Python 提交中击败了92.78%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了45.83%的用户
'''



class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # need to sort first
        sub = [()]
        for num in nums:
            sub += [item + (num, ) for item in sub]
        return list(set(sub))

'''
输入：
[4,4,4,1,4]
输出：
[[4,4,4,4],[4,4,1],[1],[4,4,4,1,4],[4,4,1,4],[4,4],[4,4,4,1],[4,4,4],[4,1,4],[],[1,4],[4],[4,1]]
预期结果：
[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
'''