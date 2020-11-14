'''
You are here!
Your runtime beats 30.81 % of python submissions.

https://docs.python.org/2/library/itertools.html#itertools.permutations
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        permuts = []
        for per in permutations(nums, len(nums)):
        # for per in permutations(nums): # also work
            permuts.append(per)
        return list(set(permuts))
    
