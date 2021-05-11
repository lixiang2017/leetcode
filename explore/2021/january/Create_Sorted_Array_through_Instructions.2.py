'''
65 / 65 test cases passed.
Status: Accepted
Runtime: 8800 ms
Memory Usage: 25.7 MB
Submitted: 0 minutes ago

You are here!
Your memory usage beats 83.93 % of python submissions.
'''


import bisect 
MOD = 10 ** 9 + 7
# MOD = int(1e9 + 7)

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        total_cost = 0
        less = greater = 0
        nums = []
        for instr in instructions:
            less = bisect.bisect_left(nums, instr)
            greater = bisect.bisect_right(nums, instr)
            total_cost += min(less, len(nums) - greater)
            nums.insert(greater, instr)
        
        return total_cost % MOD
